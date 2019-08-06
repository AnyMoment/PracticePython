#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 01:05:39 2019

@author: user
"""

#import calendar
while True:
    try:
        inputMonth=str(input("Enter an month:"))
        #how to convert name to month number
       # print("Number of days in",inputMonth,"is",calendar.monthlen(inputMonth))
        break;
    except ValueError:
        print("Enter Valid Input")


	
if inputMonth == "February":
    print("No. of days: 28/29 days")
elif inputMonth in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif inputMonth in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")