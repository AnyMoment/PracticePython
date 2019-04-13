#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
..................Write to file.................................

try:
    
    with open("//home//user//Desktop//PythonExamples/MyFile.txt",mode='x',encoding='utf-8') as MyFile:
        MyFile.write("welcome to Python")
        MyFile.writelines(" It's a good language")
        MyFile.write("Thank you")
        print("File creation sucess")
except IOError:
    print("Unable to create")
    print("server write priotected")
finally:
    print("Finally executed") 
    
    #with open("//home//user//Desktop//PythonExamples/",mode='r',encoding='utf-8')as-----
    #---------> absolute path  
    #with open("MyFileRead.txt",mode='r',encoding='utf-8')as------
    #--------->Relative path
    
    
...........................Read File Demo.........................


try:
    with open("//home//user//Desktop//PythonExamples/MyFileRead.txt",mode='r',encoding='utf-8')as  MyFile2:
        #MyFile2.write("New file")
        chars=MyFile2.read(5)
        print(chars)
        print("File read Successful")
except IOError:
    print("Unable to read. File unavailable")
 
....................Reading all lines and characters..................    
    
try:
    with open("MyFileRead.txt",mode='r',encoding='utf-8')as  MyFile2:
        #MyFile2.write("New file")
        chars=MyFile2.read()
        print(chars)
        print("File read Successful")
except IOError:
    print("Unable to read. File unavailable.")
    
....................................Length of all characters...............

try:
    with open("//home//user//Desktop//PythonExamples/MyFileRead.txt",mode='r',encoding='utf-8')as  MyFile2:
        #MyFile2.write("New file")
        #MyFile2.write("Welcome to python")
        chars=MyFile2.read()
        print(chars)
        print("Number of chars in file",len(chars))
        print("File read Successful")
except IOError:
    print("Unable to read. File unavailable")   
...........................................................
    
    
try:
    with open("//home//user//Desktop//PythonExamples/MyFileRead.txt",mode='r',encoding='utf-8')as  MyFile2:
        #MyFile2.write("New file")
        #MyFile2.write("Welcome to python")
        chars=MyFile2.readlines()
        print(MyFile2.readline())
        print(MyFile2.readlines())
    
        print("Number of chars in file",len(chars))
        print("File read Successful")
except IOError:
    print("Unable to read. File unavailable")   
"""
try:
    with open("//home//user//Desktop//PythonExamples/MyFileRead.txt",mode='r',encoding='utf-8')as  MyFile2:
        for line in MyFile2:
            print(line)
except IOError:
    print("Unable to read. File unavailable")  
