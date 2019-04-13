"""

........................Rename and deleting a file...................

import os
os.rename("a.txt","DeleteThis.txt")
print("File renamed")
os.remove("DeleteThis.txt")
print("delete successful")


............................Shutdown and restart Python................

"""

import os
check=input("Shutdown your computer?()y/n:")
if check=='n':
    exit()
else:
    os.system("shutdown /s/t 1")