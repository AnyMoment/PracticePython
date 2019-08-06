"""
......................Static...................................

class Bank():
    @staticmethod
    def Banking(Attr):
        print("Welcome to Banking")
        print("It is Static Method")
        print("Pass Attribute :",Attr)
BB=Bank()
BB.Banking("Citi")
BB.Banking("BOA")

.........................GarbageCollection..................
"""
class Dog():
    def Sound(self):
        print("Bark")

class Cat():
    def Sound(self):
        print("Mew")
    def __del__(self):
        print("Destructor")

d=Dog()
d.Sound()
c=Cat()
c.Sound()
del c