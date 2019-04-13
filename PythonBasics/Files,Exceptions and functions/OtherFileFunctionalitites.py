"""
......................appending a file.............


try:
    with open('NewFile.txt','a') as f:
        f.writelines("This is a new line\n")
        f.writelines("This is a new line2\n")
        f.writelines("This is a new line3\n")
except IOError:
    print("Error")

.......................tell method..................
try:
    with open('NewFile.txt','r') as f:
        print(f.read(5))
        print(f.tell())
        print(f.read(10))
        print(f.tell())
        print("file read successful")
except IOError:
    print("Error")

......................seek method..................


try:
    with open('NewFile.txt','r') as f:
        print(f.read(5))
        print(f.tell())
        print(f.read(10))
        print(f.tell())
        f.seek(0,0)
        print(f.read(5))
        print(f.tell())
        print("file read successful")
except IOError:
    print("Error")
"""