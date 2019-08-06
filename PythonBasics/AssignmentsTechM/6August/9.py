#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 02:10:26 2019

@author: user
"""
while True:
    try:
        input_=int(input("Enter a number:"))
        break;
    except Exception as arg:
        print(arg)
        
        
a=0
b=1
count=0
if input_<0: 
        print("invalid")
elif input_==1:
        print (0)
else:
    while count < input_:
        print(a)
        c=a+b
        a=b
        b=c
        count=count+1

