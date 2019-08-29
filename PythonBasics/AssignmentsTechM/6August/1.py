
      
while True:
      try:
           numInput=int(input("Please Enter a number:"))
           break
      except ValueError:
           print("Try Again")
           

if numInput>=0:
     print("positive")
elif numInput==0:
        print("Zero")
else:
      print("negative")
                         
           
      
      
