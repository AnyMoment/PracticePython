
      
while True:
      try:
           numInput=int(input("Please Enter a number to check :"))
           numRange=int(input("Please Enter a inner limit of range:"))
           numRange2=int(input("Please Enter the outer limit of range:"))
           break
      except ValueError:
           print("Try Again")
           

if numInput > 1:
     for i in range(2,numInput):
       if (numInput % i) == 0:
             break
     else:
       print(numInput,"is a prime number")
else:
   print(numInput,"is not a prime number")  
   
   print("List of prime numbers in entered ranges are:")
                       
for i in range(numRange,numRange2+1):
      if i>1:           
            for j in range(2,i):
                  if (i % j)== 0:
                    break
            else:
                  print(i)
           
       
