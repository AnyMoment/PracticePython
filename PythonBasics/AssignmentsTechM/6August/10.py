
      
while True:
      try:
           numInput=int(input("Please Enter a outer limit:"))
           break
      except ValueError:
           print("Try Again")
sum=0           
for i in range (1,numInput+1):
     sum=sum+i
     print(sum)
