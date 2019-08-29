
      
while True:
      try:
           numInput=int(input("Please Enter a number to check :"))
           break
      except ValueError:
           print("Try Again")
           
for i in range (1,11):
      print(numInput,"*",i,"=",numInput*i)
