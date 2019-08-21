
# Insert ',' between characters and ignore spaces 
#Machine Learning; o/p= M,a,c,h,i,n,e,L,e,a,r,n,i,n,g, 
import re


str=input("Enter a string:")
str=re.sub(r"(\s)",r"",str)
print(str)
x= re.sub(r"([a-z]|[A-z])",r"\1,",str)
print(x)
