"""
........................Lamda Functions................

x=lambda x:x**2;print(x(2))

#Max value of a set of numbers

Max=lambda x,y:x if x>y else y; print(Max(23,34))

....................List Comprehensions vs  Lambda functions..........

"""
n=[2,3,4,5,6]
print(type(n))
print(list(map(lambda x:x**2,n)))

OldList=[2,3,4,5,6]
print(type(OldList))
print(OldList)
NewList=list(map(lambda x:x**2,OldList))
print(type(NewList))
print(NewList)


