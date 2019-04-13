"""
............................File opening

FileObj=open("newDocument.txt",encoding="UTF-8")
#/home/user/Desktop/PythonExamples
print(FileObj.name)
print(FileObj.mode)
print(FileObj.closed)

FileObj=open("newDocument.txt",mode='r',encoding="UTF-8")
#/home/user/Desktop/PythonExamples
print(FileObj.name)
print(FileObj.mode)
print(FileObj.closed)

........................File opening with Exception Handling
try:
    FileObj=open("newDocument.txt",encoding="UTF-8")
#/home/user/Desktop/PythonExamples
    print(FileObj.name)
    print(FileObj.mode)
    print(FileObj.closed)
except IOError:
    print("No file found")

finally:
    print("Finally block successful")

..........................Open a file without risking non closure...                

try:
    with open("newDocument.txt",mode='r',encoding="UTF-8") as FileObj:
#/home/user/Desktop/PythonExamples
        print(FileObj.name)
        print(FileObj.mode)
        print(FileObj.closed)
except IOError:
    print("No file found")

finally:
    print("Finally block successful")
"""
