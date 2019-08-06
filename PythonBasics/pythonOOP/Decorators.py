"""
Python Decorators

Decorator is  a fucntion that takes another function and extends the behavior 
of the latter function without explicitly modifying it

INPUT fn==> DECORATOR fn ==> Output fn with extended functionality.

A decorator is a callable that returns a callable. 
A decorator takes in a fucntion, adds some functionality
and reutrns it. Decorators help to make our code shorter and better. 
"""
def DivUpdate(func):
      def Inner(a,b):
        if b==0:
            print("Unable to compute")
        else:
            return func(a,b)
      return Inner

@DivUpdate
def Div(x,y):
    return x/y
   
print(Div(12,1))
print(Div(2,2))
print(Div(2,0))  #Zero Division Error
