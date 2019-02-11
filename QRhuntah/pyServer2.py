import time
import easygopigo3
import socket
from _thread import *
import sys

#Receive messages from Qt widget
class tcpServer:

    def __init__(self):


        self.host = ''
        self.port = 5560
        self.gpg = easygopigo3.EasyGoPiGo3()
        self.main1()

    def setupServer(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
        try:
            self.s.bind((self.host, self.port))
        except socket.error as msg:
            print(msg)
        print("Socket bind complete")
        return self.s

    def setupConnection(self):
            s.listen(10) #Allows one connection at a time.
            conn, address = s.accept()
            print("Connected to: " + address[0] + ":" + str(address[1]))
            return conn

    def REPEAT(self, dataMessage):
            reply = dataMessage[1]
            return reply

    def threaded_client(self, conn):

        manualControl = False

        print("threadissa")
        while True:

                data = conn.recv(1024)
                data = data.decode('utf-8')
                dataMessage = data.split(' ', 1)
                #split the data such that you separate the command from rest
                command = dataMessage[0]

                if command == 'REPEAT':
                    reply = self.REPEAT(dataMessage)
                elif command == 'EXIT':
                    print("Client left")
                    break
                elif (command == 'KILL') or (not data) :
                    print("server shutting down")
                    self.gpg.stop()
                    #s.close()
                    break
                else:
                    reply = "Unknow command"

                conn.sendall(str.encode("ok"))
                print("Data has been sent!")

                if dataMessage[1] == "CMD":
                    manualControl = not manualControl

                if manualControl == True:
                    if dataMessage[1] == "87":
                        self.gpg.forward()
                    elif dataMessage[1] == "68":
                        self.gpg.right()
                    elif dataMessage[1] == "65":
                        self.gpg.left()
                    elif dataMessage[1] == "83":
                        self.gpg.backward()
                    elif dataMessage[1] == "STOP":
                        print("stop this shit")
                        self.gpg.stop()
                    else:
                        print("Manual Control ON")

        print("Thread killed")
        conn.close()

    def openThread(self, s):
        while True:
                print("THREAD1")
                conn, addr = s.accept()
                print("connected to: " + addr[0] + ":" + str(addr[1]))
                start_new_thread(self.threaded_client, (conn,))

    def main1(self):
        self.gpg.stop()
        print("hello from class")
        s = self.setupServer()
        s.listen(5)

        start_new_thread(self.openThread, (s,))
'''
        while True:

            try:
                print("Mainissa loop")
                time.sleep(2)
                #conn = setupConnection()
                #dataTransfer(conn)

            except:
                print("ERROR OCCURED")
                self.s.close()
                break
'''
'''
x = tcpServer()
while True:
    print("kippo")
    time.sleep(2)
'''
