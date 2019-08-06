#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 02:40:54 2019

@author: user
"""

list_=[]
for k in range(0,3):
    i=int(input("input a number"))
    list_.append(i)
list_.sort()
print("largest number is",list_[2])