# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:27:46 2021

@author: phamt
"""


def dec2bin(n):
    result = ""
    
    while n > 0:
       r = n % 2
       n = n // 2
       result = str(r) + result
    return result   
    
       
    
x = int(input("enter a number:"))
print(dec2bin(x))

HEllo world

    
    
    
