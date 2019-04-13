"""
.........................assertions......................
def power(x,y):
    assert x>0,"x must be a postive number not {0}"
    assert y>0, "y must be a positive non zero number"
    return x**y
print(power(1,2))
print(power(1,1))
print(power(1,-1))

....................Exception as arguments
"""
try:
    x=int(input("enter any integer:"))
    y=int(input("enter any integer:"))
    z=x/y 
except ValueError:
    print("No alphabets")
except Exception as arg:
    print("error", arg)
    
"""
........................try except else..........................    
    
try:
    x=int(input("enter any integer:"))
    y=int(input("enter any integer:"))
    z=x/y
    print("printing z",z)
except:
    pass
    print("Error:Arithmetic operation ignored.Pass block")
else:
    print("successful")
    
....................raise an error..........

x=int(input("enter any integer:"))
y=int(input("enter any integer:"))
if y==0:
    raise ZeroDivisionError('Sorry Unable to compute')
else:
    z=x/y
    print(z)
"""     