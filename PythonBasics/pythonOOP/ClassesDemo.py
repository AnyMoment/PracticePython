"""
...............................Different Syntaxes to create a class........
#syntax1
class Account:
    pass
my_account=Account()
your_account=Account()

#Syntax2
class Account(object):
    pass
my_account=Account()
your_account=Account()

#Syntax3
class Account():
    pass
my_account=Account()
your_account=Account()

...............................Print an object 

class Employee1:
    pass
MyIns1=Employee1()
print(MyIns1)

.................................Self................
self argument represnets the actual instance of the class when you create an instance
of a class, using that instance we can call methods, whernever method gets  call via instance,
the interpreter sends the very first argument as self while calling methods,
self argument always pass interpreter implicitly.

...................................
class Msg():
    def Wish(self):
        print("Hello")
        print("Thank you")
        
MM=Msg()
MM.Wish()
"""
