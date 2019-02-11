import myImport

#Example
#Create a class named MyClass, with a data member named myDataMemeber
class Dog:
     
    numberOfDogs = 0

    def __init__(self, name):
#instance variable unique to each instance
        
        self.name = name
        Dog.numberOfDogs += 1
        print (name)

    def setAttr(self, attr):
        Dog.numberOfDogs = attr

    def getAttr(self):
            print ("Parent attribute :", Dog.numberOfDogs)  

    def setData (self, age):
        self.age = age

    def getData (self):
        print (self.age)

    def myfunc(self):
        print("Hello my name is " + self.name)

    def parentMethod(self):
        print ("Calling parent method")

    def __del__(self):
        print (self, "MyClass object destroyed")

class Child(Dog):
    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ("Calling child method")

def main():
#function_docstring
    j = myImport.job("maansiirto")
    j.show_job()

    
   
    



if __name__ == '__main__':
    main()
