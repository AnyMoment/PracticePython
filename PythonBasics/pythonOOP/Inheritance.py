"""
#..........................Single level Inheritance
class Animal():
    def eat(self):
        print("Every animal eats")
class dog(Animal):
    def sound(self):
        print("barking")
        
d=dog()
d.eat()
d.sound()


class animal:
    def __init__(self,name):
        self.name=name
class dog(animal):
    def display(self):
        print("Hello",self.name)
d=dog("Puppy")
d.display()


........................Mulli Level Inheritance.......

"""
class FinancialServicesIn():
    def FSI(self):
        print("Finance Matters, every org need spermission from them")
class ReserveBankofIndia(FinancialServicesIn):
    def RBI(self):
        print("I need to follow FSI rules")
class CoreBanking(ReserveBankofIndia):
    def SBI(self):
        print("I must follow RBI Rules")
        
CB=CoreBanking()
CB.FSI()
CB.RBI()
CB.SBI()