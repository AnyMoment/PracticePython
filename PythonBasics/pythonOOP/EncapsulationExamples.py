"""
....Returns attribute error because it is private......
class IT():
    def __init__(self):
        print("Hello Default")
        self.__x=100
i=IT()
print(i.__x)


.....................protected class private attribute.............
class IT():
    def __init__(self):
        print("Hello Default")
        self.__x=100
i=IT()
#print(i.__x)
print(i._IT__x)



..........Calling a private method in a public/default constructo........
class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("I am driving")
    def __updatesoftware(self):
        print("Car software updated")
        
blackcar=car()
blackcar.drive()

......Using private methods and variables, manipulating private attributes
        inside a clas....................................

class car_details():
    __maxspeed=0
    __name=""
    #Instance Variables  of Attributes
    def __init__(self):
        self.__maxspeed=300
        self.__name="SportsCar"
    #Calling private attributes inside the class
    def CarDetails(self):
        print("Car model is:",self.__name)
        print("Car speed is:",self.__maxspeed)
        print("Thank you")
    #redefining car speed
    def SetSpeed(self,speed):
        self.__maxspeed=speed
        print("Current (new) car speed is",self.__maxspeed)
        print("goodbye")

c=car_details()
c.CarDetails()
c.SetSpeed(100)
"""



        