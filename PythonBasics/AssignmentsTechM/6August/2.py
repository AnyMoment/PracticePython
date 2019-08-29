
      
while True:
      try:
           numInput=int(input("Please Enter a number:"))
           break
      except ValueError:
           print("Try Again")
           

if numInput%2==0:
     print("even")
else:
      print("odd")
                         
           
      
      
