"""
................................Access Modifiers..........................


...........#Public

class Attributes():
    def __init__(self):
        self.Public="Hello I am Public"
AA=Attributes()
print(AA.Public)

AA.Public=AA.Public+':add this too'   #Public Attribute Can be updated
print(AA.Public)

#..........Protected

class Attributes():
    def __init__(self):
        self._Protect="Hello I am Protected"
AA=Attributes()
print(AA._Protect)

............#Private

..........................#throws an Attribute Error

class Attributes():
    def __init__(self):
        self.__private="Hello I am Protected"
        
AA=Attributes()
print(AA.__private)


...............................getattr()......................

class Attributes():
    Name="Python"
    ID=1

aa=Attributes()

print("Attribute 1 is",getattr(aa,"Name"))
print("Attribute 2 is",getattr(aa,"ID"))
#RunTime Assignment
print("Attribute 3 is",getattr(aa,"gender","Male"))
attr=getattr(aa,"state","Florida")
print("Attribute 4 is",attr)

.................................setattr().....................

class Attributes():
    Name="Python"
    ID=1

aa=Attributes()

print("Attribute 1 is",getattr(aa,"Name"))
print("Attribute 2 is",getattr(aa,"ID"))
attr1=setattr(aa,"Name","Florida")
print("Attribute 1 after change is",attr1)
print("Attribute 2 after changes are",setattr(aa,"ID","35324"))

....................................hasattr()...............

class Attributes():
    Name="Python"
    Id=1
aa=Attributes()
print(hasattr(aa,'Name'))
print(hasattr(aa,'name'))

....................................delattr()....................


class Attributes():
    Name="Python"
    ID=1 
aa=Attributes()
delattr(aa,'Name')
print(hasattr(aa,"Name"))
"""

