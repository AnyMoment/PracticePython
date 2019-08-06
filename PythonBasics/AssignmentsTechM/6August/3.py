#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 01:05:39 2019

@author: user
"""

import calendar
while True:
    try:
        inputYear=int(input("Enter an year:"))
        break;
    except ValueError:
        print("No alphabets")

if inputYear/100<1:
            print("enter a year with centuary")
      
elif calendar.isleap(inputYear)==True:
    print(inputYear,"is a leap year")
else:
    print(inputYear,"isn't a leap year")
 
   