import easygopigo3
import pyServer2
import time
import twitterBot
import mySql_insert
import barcode_scanner_video

class RobotMovement(object):
    """docstring for RobotMovement"""
    def __init__(self):
        super(RobotMovement, self).__init__()
        self.gpg = easygopigo3.EasyGoPiGo3()
        self.my_distance_sensor = self.gpg.init_distance_sensor()
        self.matrix = [[0,0,0,0,],
                  [0,0,0,0,],
                  [0,0,0,0,],
                  [0,0,0,0,]]
        self.current_position = [0][0]
        self.x = 0
        self.y = 0
        self.start = [0][0]
        self.goal = [0][0]
        self.degree = 90
        self.distance = 30

    def print_matrix(self):
        for row in self.matrix:
            print (' '.join(map(str,row)))

    def object_detected(self,x,y):
        self.gpg.turn_degrees(self.degree)
        if self.object_detection(self.distance):
            self.gpg.turn_degrees(self.degree)
        elif not self.object_detection(self.distance):
            self.gpg.drive_cm(self.distance)
            self.y += 1
        else:
            self.gpg.drive_cm(self.distance)
            self.y += 1

    def forward(self, distance,x,y):
        if self.object_detection(distance):
            print("Object detected")
            self.object_detected(x,y)
        else:
            print("Going forward")
            self.gpg.drive_cm(distance)
            x += 1

    def object_detection(self, distance):
        measurement = self.my_distance_sensor.read_mm()
        if measurement < distance * 10:
            return True
        else:
            return False

    def raw_distance(self):
        measurement = self.my_distance_sensor.read_mm()
        return measurement


    def matrix_mapping(self):
        self.current_position = self.matrix[self.x][self.y]
        print(self.current_position)

    def run(self):
        self.forward(30,self.x, self.y)
        self.print_matrix()

def main():

    server = pyServer2.tcpServer()

    #twitterBot.dl_image() #Insert QR code to twitter
    #gpg = easygopigo3.EasyGoPiGo3()
    gpg = RobotMovement()
    while True:
        measurement = gpg.raw_distance()
        print("Distance is " + str(measurement))
        #gpg.run()
        #gpg.matrix_mapping()
        time.sleep(1)
        if measurement < 50:
            QRmsg = barcode_scanner_video.readQR()
            if QRmsg is None:
                print("No Qr code")
            else:
                mySql_insert.insertdata(QRmsg)
                twitterBot.dl_image(QRmsg)
        print("matrice loopp")


if __name__ == '__main__':
    main()
