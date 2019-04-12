"""
#Read 5 subjects, display failed status, otherwise compute average and display grade 
import time 



import functools
subjectMarks= [int(x) for x in input("Enter Subjects seperated by space:").split()]
print("Subject marks entered are:",subjectMarks)
startTime=time.clock()
temp=list(filter(lambda x: x>50,subjectMarks))
if subjectMarks==temp:
      averageSubjects= functools.reduce(lambda x,y: x+y,subjectMarks)/float (len(subjectMarks))
      print("The average is",averageSubjects)
      if averageSubjects > 80 :
            print("grade A")
      elif averageSubjects > 70 :
            print("grade B")
      elif averageSubjects > 50:
            print("grade C")
else:
      print("Failed a subject, result not caluculated")          

print("%s" %(time.clock()-startTime))
""" 
def MyfunMod1():
      print("welcome to module 1")
      return
def MyfunMod2():
      print("Welcome to module 2")
      return
c=10
d=23
def add(a,b):
      return(a+b)
def sub(a,b):
      return(a-b)
def div(a,b):
      return(a/b)
def mul(a,b):
      return(a*b)

      
       
       


     