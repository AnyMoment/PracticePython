"""
................default args......................

def myfun(a,b):
    print(a+b)
    return 
print(myfun(1,2))
print('........................')

def defaultargs(a=100,b=10,c=1):
    print(a,b,c)
    print(b,c)
    print(c)
    return
print('........................')
defaultargs(7,4,3)
print('........................')
defaultargs()
print('........................')
defaultargs(c=13,b=34,a=45)
print('........................')
defaultargs(0,1) 

def printi(name, exp='15+'):
    print("Name:",name)
    print("experience:",exp)
    return
printi(exp=14,name="KSRaju")
printi(name="nareshIT")

....................Arbitary args.....................


def Arbitary_args(*a):
    for x in a:
        print(x)
    return 
Arbitary_args()
Arbitary_args(1)
Arbitary_args(1,2,3,4,7)


def arb_args(*arr):
    for item in arr:
        print(item)
    return()
arb_args()
arb_args("String1",3,"Python")

#....................Local and Global Scopes.................

x= int(input("Enter:"))
def LocalScope1():
    y=200
    print(x+y)
    return
def LocalScope2():
    x=20
    y=30
    print(x+y)
    print(id(x))
    return
LocalScope1()
print(id(x))
LocalScope2()


#.................Global Keyword............................


def myfun():
    global a
    a=100
    b=10
    print(a+b)
    return
def myfun1():
    b=20
    print(a+b)
    return


.............................Nested Functions............

def Outerfn():
    print("hello Outer")
    def Innerfn():
        print("Hello Inner")
    Innerfn()
Outerfn()

................with parameters being paased................
    
def Outerfn():
    x=1
    def Innerfn(a):
        print(a+x)
    Innerfn(2)
Outerfn()


def Outerfn():
    x=1
    def Innerfn(a):
        print(a+x)
    print(x) # this is execcuted first as it is part of the outer function   
    Innerfn(2)
Outerfn()

"""































