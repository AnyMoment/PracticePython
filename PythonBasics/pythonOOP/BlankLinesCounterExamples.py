
#number of characters in file without spacing 

Linelist= list()
try:
      with open("Newfile.txt",'w') as File1:
            File1.write("This is line 1")
            File1.write("This is line 2")
            
except IOError:
      print("Write error")
      
#LineList=list()
with open('Newfile.txt','r',encoding='UTF-8') as f:
                                 
            y=0
            print("inside read")
            try:           
                  for word in f:
                       
                        print(word)
                        word=word.strip()
                        word=word.replace(" ","")
                        x=len(word)
                        y=y+x
                  print("The number of characters are:",y)   
            except:
                  print('no error')
                  
 
#Number of blank lines in  a file

with open('Newfile.txt','r',encoding='UTF-8') as f:
                                 
            y=0
            print("inside read")
            try:           
                  for word in f:
                       
                        print(word)
                        if word.split()==[]:
                              y+=1
                  print("Empty lines are:",y)
                  
            except:
                  print('no error')                 

                  


