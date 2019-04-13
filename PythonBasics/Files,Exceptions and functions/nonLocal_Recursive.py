"""
...............nonLocal...............

def OuterFunction():
    a=10
    print("the value is", a)
    def InnerFunction():
        a=20
        print("the value is",a)
    InnerFunction()
OuterFunction()

#Use of NonLocal

def OuterFunction():
    a=10
    print("the value is", a)
    def InnerFunction():
        nonlocal a
        a=20
        print("the value is",a)
    InnerFunction()
    print("the value is", a)
OuterFunction()


.............................Recursive Function............


def Factorials(n):
    if n==1:
        return 1
    else:
        return n*Factorials(n-1)
print(Factorials(3))

"""