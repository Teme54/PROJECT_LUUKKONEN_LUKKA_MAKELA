#############################################################################
# WAVEFRONT ALGORITHM
# Adapted to Python Code By Darin Velarde
# Fri Jan 29 13:56:53 PST 2010
# from C code from John Palmisano
# (www.societyofrobots.com)
############################################################################
try:
    import numpy
except:
    print("The numpy math library is not installed.")
try:
    import easygopigo3
except:
    print("The easygopigo3 library is not installed.")
import time
############################################################################


class waveFrontPlanner:

    def __init__(self, slow=False):
        self.__slow = slow
        self.__map = [[000, 999, 000, 000, 000, 000, 000],\
                      [000, 999, 000, 000, 000, 000, 000],\
                      [000, 999, 000, 000, 000, 000, 000],\
                      [000, 999, 000, 000, 000, 000, 000],\
                      [000, 999, 000, 000, 000, 000, 000],\
                      [000, 999, 000, 000, 000, 000, 000],\
                      [000, 000, 000, 000, 000, 000, 000]]
        if str(type(map)).find("numpy") != -1:
            #If its a numpy array
            self.__height, self.__width = self.__map.shape
        else:
            self.__height, self.__width = len(self.__map), len(self.__map[0])

        self.__nothing = 0
        self.__wall = 999
        self.__goal = 1
        self.__path = "PATH"

        self.distance = 10 #Distance to travel

        self.__finalPath = []

        self.gpg = easygopigo3.EasyGoPiGo3()
        self.my_distance_sensor = self.gpg.init_distance_sensor()

        #Robot value
        self.__robot = 254
        #Robot default Location
        self.__robot_x = 0
        self.__robot_y = 0

        #default goal location
        self.__goal_x = 0
        self.__goal_y = 0

        #temp variables
        self.__temp_A = 0
        self.__temp_B = 0
        self.__counter = 0
        self.__steps = 0 #determine how processor intensive the algorithm was

        #when searching for a node with a lower value
        self.__minimum_node = 250
        self.__min_node_location = 250
        self.__new_state = 1
        self.__old_state = 1
        self.__reset_min = 250 #above this number is a special (wall or robot)

        #Robots movement states
        self.forward = False
        self.backward = False
        self.turned_left = False
        self.turned_right = False
        self.stopped = True

        #Robots orientation
        self.__orientation = 0
        self.gpg.set_speed(200)
        self.degree = 94
    ###########################################################################

    def __del__(self):
        self.path = "PATH"
        print("Object deleted!")

    def object_detection(self, distance):
        measurement = self.my_distance_sensor.read_mm()
        if measurement < distance * 10:
            return True
        else:
            return False

    def setRobotPosition(self, x, y):
        """
        Sets the robot's current position

        """

        self.__robot_x = x
        self.__robot_y = y
    ###########################################################################

    def setGoalPosition(self, x, y):
        """
        Sets the goal position.

        """

        self.__goal_x = x
        self.__goal_y = y
    ###########################################################################

    def robotPosition(self):
        return  (self.__robot_x, self.__robot_y)
    ###########################################################################

    def goalPosition(self):
        return  (self.__goal_x, self.__goal_y)
    ###########################################################################

    def orientation_(self):
        self.__orientation = self.__orientation + self.degree
        print(self.__orientation)
        if self.__orientation == 360:
            self.orientation = 0
            print(self.__orientation)
        if self.__orientation == -360:
            self.__orientation = 0
            print(self.__orientation)

    def orientation_correction(self):
        orientation = 360 - self.__orientation
        if self.goalPosition() == "(0, 0)":
            return
        if orientation > 0:
            correction = 360 - orientation
            correction = int(round(correction / 90))
            print(correction)
            self.gpg.turn_degrees(correction*self.degree)
        if orientation < 0:
            correction = 360 + orientation
            correction = int(round(correction / 90))
            print(correction)
            self.gpg.turn_degrees(-correction)*self.degree
        if orientation == 0:
            return



    def run(self, prnt=False):
        """
        The entry point for the robot algorithm to use wavefront propagation.

        """
        path = []
        self.orientation_correction()
        while self.__map[self.__robot_x][self.__robot_y] != self.__goal:
            print("Just driving around")
            if not self.forward and not self.backward:
                self.stopped = True
            if self.__steps > 20000:
                print("Cannot find a path")
                return
            #find new location to go to
            self.__new_state = self.propagateWavefront()
            #update location of robot
            if self.__new_state == 1:
                self.__robot_x -= 1
                if self.turned_left:
                    self.gpg.turn_degrees(-self.degree)
                    self.orientation_()
                    self.turned_left = False
                if self.turned_right:
                    self.gpg.turn_degrees(self.degree)
                    self.orientation_()
                    self.turned_right = False
                self.backward = True
                self.gpg.drive_cm(self.distance)
                if prnt:
                    print("Move to x=%d y=%d\n\n" % \
                        (self.__robot_x, self.__robot_y))
                path.append((self.__robot_x, self.__robot_y))
            if self.__new_state == 2:
                self.__robot_y += 1
                if self.forward:
                    self.gpg.turn_degrees(-self.degree)
                    self.orientation_()
                    self.gpg.drive_cm(self.distance)
                    self.forward = False
                    self.turned_left = True
                elif self.backward:
                    self.gpg.turn_degrees(self.degree)
                    self.orientation_()
                    self.gpg.drive_cm(self.distance)
                    self.backward = False
                    self.turned_left = True
                elif not self.turned_left:
                    self.gpg.turn_degrees(-self.degree)
                    self.orientation_()
                    self.turned_left = True
                else:
                    self.gpg.drive_cm(self.distance)
                print("Move to x=%d y=%d\n\n" % \
                        (self.__robot_x, self.__robot_y))
                path.append((self.__robot_x, self.__robot_y))
            if self.__new_state == 3:
                self.__robot_x += 1
                if self.turned_left:
                    self.gpg.turn_degrees(self.degree)
                    self.orientation_()
                    self.turned_left = False
                if  self.turned_right:
                    self.gpg.turn_degrees(-self.degree)
                    self.orientation_()
                    self.turned_right = False
                self.forward = True
                self.gpg.drive_cm(self.distance)
                if prnt:
                    print("Move to x=%d y=%d\n\n" % \
                        (self.__robot_x, self.__robot_y))
                path.append((self.__robot_x, self.__robot_y))
            if self.__new_state == 4:
                self.__robot_y -= 1
                if self.forward:
                    self.gpg.turn_degrees(self.degree)
                    self.orientation_()
                    self.gpg.drive_cm(self.distance)
                    self.forward = False
                    self.turned_right = True
                elif self.backward:
                    self.gpg.turn_degrees(-self.degree)
                    self.orientation_()
                    self.gpg.drive_cm(self.distance)
                    self.backward = False
                    self.turned_right = True
                elif not self.turned_right:
                    self.gpg.turn_degrees(self.degree)
                    self.orientation_()
                    self.turned_right = True
                else:
                    self.gpg.drive_cm(self.distance)
                if prnt:
                    print("Move to x=%d y=%d\n\n" % \
                        (self.__robot_x, self.__robot_y))
                path.append((self.__robot_x, self.__robot_y))
            self.__old_state = self.__new_state
            #input()
        msg = "Found the goal in %i steps:\n" % self.__steps
        msg += "Map size= %i %i\n\n" % (self.__height, self.__width)
        #self.gpg.turn_degrees(191)
        self.orientation_correction()
        time.sleep(5)
        if prnt:
            print(msg)
            self.printMap()
        return path
    ###########################################################################

    def propagateWavefront(self, prnt=False):
        """


        """

        self.unpropagate()
        #Old robot location was deleted, store new robot location in map
        self.__map[self.__robot_x][self.__robot_y] = self.__robot
        self.__path = self.__robot
        #start location to begin scan at goal location
        self.__map[self.__goal_x][self.__goal_y] = self.__goal
        counter = 0
        while counter < 200:  #allows for recycling until robot is found
            x = 0
            y = 0
            time.sleep(0.00001)
            #while the map hasnt been fully scanned
            while x < self.__height and y < self.__width:
                #if this location is a wall or the goal, just ignore it
                if self.__map[x][y] != self.__wall and \
                    self.__map[x][y] != self.__goal:
                    #a full trail to the robot has been located, finished!
                    minLoc = self.minSurroundingNodeValue(x, y)
                    if minLoc < self.__reset_min and \
                        self.__map[x][y] == self.__robot:
                        if prnt:
                            print("Finished Wavefront:\n")
                            self.printMap()
                        # Tell the robot to move after this return.
                        return self.__min_node_location
                    #record a value in to this node
                    elif self.__minimum_node != self.__reset_min:
                        #if this isnt here, 'nothing' will go in the location
                        self.__map[x][y] = self.__minimum_node + 1
                #go to next node and/or row
                y += 1
                if y == self.__width and x != self.__height:
                    x += 1
                    y = 0
            #print self.__robot_x, self.__robot_y
            if prnt:
                print("Sweep #: %i\n" % (counter + 1))
                self.printMap()
            self.__steps += 1
            counter += 1
        return 0
    ###########################################################################

    def unpropagate(self):
        """
        clears old path to determine new path
        stay within boundary

        """

        for x in range(0, self.__height):
            for y in range(0, self.__width):
                if self.__map[x][y] != self.__wall and \
                    self.__map[x][y] != self.__goal and \
                    self.__map[x][y] != self.__path:
                    #if this location is a wall or goal, just ignore it
                    self.__map[x][y] = self.__nothing #clear that space
    ###########################################################################

    def minSurroundingNodeValue(self, x, y):
        """
        this method looks at a node and returns the lowest value around that
        node.

        """

        #reset minimum
        self.__minimum_node = self.__reset_min
        #down
        if x < self.__height -1:
            if self.__map[x + 1][y] < self.__minimum_node and \
                self.__map[x + 1][y] != self.__nothing:
                #find the lowest number node, and exclude empty nodes (0's)
                self.__minimum_node = self.__map[x + 1][y]
                self.__min_node_location = 3
        #up
        if x > 0:
            if self.__map[x-1][y] < self.__minimum_node and \
                self.__map[x-1][y] != self.__nothing:
                self.__minimum_node = self.__map[x-1][y]
                self.__min_node_location = 1
        #right
        if y < self.__width -1:
            if self.__map[x][y + 1] < self.__minimum_node and \
                self.__map[x][y + 1] != self.__nothing:
                self.__minimum_node = self.__map[x][y + 1]
                self.__min_node_location = 2
        #left
        if y > 0:
            if self.__map[x][y - 1] < self.__minimum_node and \
                self.__map[x][y - 1] != self.__nothing:
                self.__minimum_node = self.__map[x][y-1]
                self.__min_node_location = 4
        return self.__minimum_node
    ###########################################################################

    def printMap(self):
        """
        Prints out the map of this instance of the class.

        """

        msg = ''
        for temp_B in range(0, self.__height):
            for temp_A in range(0, self.__width):
                if self.__map[temp_B][temp_A] == self.__wall:
                    msg += "%04s" % "[#]"
                elif self.__map[temp_B][temp_A] == self.__robot:
                    msg += "%04s" % "-"
                elif self.__map[temp_B][temp_A] == self.__goal:
                    msg += "%04s" % "G"
                else:
                    msg += "%04s" % str(self.__map[temp_B][temp_A])
            msg += "\n\n"
        msg += "\n\n"
        print(msg)
        #
        if self.__slow == True:
            time.sleep(0.05)
###############################################################################

if __name__ == "__main__":

    '''floormap = [[000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000],\
                [000, 000, 000, 000, 000, 000, 000]]'''
    """
    X is vertical, Y is horizontal

    """

    '''floormap = [[000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000],\
                [000,000,000,000,000,000,000,000,000,000,000,000]]'''

    #start = time.time()
    planner = waveFrontPlanner(False)
    planner.setGoalPosition(0, 6)
    print(planner.goalPosition())
    print(planner.robotPosition())
    planner.run(True)
    print(planner.robotPosition)
    del planner

    planner = waveFrontPlanner(False)
    #print(planner1.robotPosition)
    #print(planner1.goalPosition)
    planner.setRobotPosition(0, 6)
    planner.setGoalPosition(0, 0)
    print(planner.robotPosition)
    print(planner.goalPosition)
    planner.run(True)