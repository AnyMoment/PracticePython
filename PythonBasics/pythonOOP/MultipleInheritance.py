"""
Method Resolution Order

In the multiple inheritance scenario, any specified attribute is searched  first
in the current class.If not found, the search continues into parent class in depth first
left-right fashion without searching same class twice.  


class LandLive():
    def LandLife(self):
        print("It can live on land")
        print("Good")
class WaterLive():
    def WaterLife(self):
        print("Lives in water")
class Frog(LandLive,WaterLive):
    pass
F=Frog()
F.LandLife()
F.WaterLife()

.....................................................................

"""
class A():
    def MyMethod(self):
        print("Class A")
class B():
    pass
class C(B,A):
    print("Class C")
    pass
def main():
    Obj1=C()
    Obj1.MyMethod()

if __name__=="__main__":
    main()
    

