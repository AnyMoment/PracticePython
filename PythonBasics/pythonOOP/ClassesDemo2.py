"""
class Exceptions_Class():
    def Try_Except(self):
        try:
            x=int(input("Enter any number:"))
            y=int(input("Enter any number:"))
            z=x/y
            print("Result:",z)
        except ValueError:
            print("Invalid error")
        except ZeroDivisionError:
            print ("not zero")
        finally:
            print("Finally block")

#Creating Instance            
EE=Exceptions_Class()
#Calling method with Object
EE.Try_Except()
EE.Try_Except()


...................................__init()__.................................

class Hello_Wish():
    def __init__(self):
        print("This is a default constructor")
        print("This is always called first")
    def GoodBye(self):
        print("This is called next")
HH=Hello_Wish()
HH.GoodBye()
.........................

class Cal():
    def __init__(self,a,b): # def __init__(c,a,b) [Called Alternatively]
        print("This is a default constructor")
        print("Result:",(a+b))
    def GoodBye(self):
        print("This is called next")
HH=Cal(2,3)
HH.GoodBye()

..........................
class person:
    def __init__(self,name):
        #Instance variable
        self.name=name
    
    def display(self):
        print("Hello",self.name)
        return
Myobj=person(" Python")
Myobj.display()

.........................built in attributes...................................

class BuiltinAttrs():
   #docString
print(BuiltinAttrs.__dict__)
print(BuiltinAttrs.__doc__)    
print(BuiltinAttrs.__name__)
print(BuiltinAttrs.__bases__)
print(BuiltinAttrs.__module__)


..................................User Defined Attributes...................


class Employee():
    empCount=0
print(Employee.empCount)
obj=Employee()
print(obj.empCount)
obj.newCount=30
print(obj.newCount)






