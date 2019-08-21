"""
from moduleDemo1 import c,add
print(c)
print(add(3,4))
"""

from moduleDemo1 import *
print(add(3,4))
print(sub(3,4))
print(mul(3,4))
print(div(3,4))

#print(dir(a))

e=34
print(dir(e))

print(__file__)
print(__doc__)
print(__builtins__)

import os 
print(os.getcwd)
print(os.getcwdb)
