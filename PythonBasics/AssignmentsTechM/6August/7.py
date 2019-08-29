
      
while True:
      try:
           numInput=int(input("Please Enter a number to check :"))
           break
      except ValueError:
           print("Try Again")
           
fact =1 
while numInput!=0:
      fact=fact*numInput
      numInput=numInput-1

print(fact)

