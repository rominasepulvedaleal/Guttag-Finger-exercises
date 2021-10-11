#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:17:38 2021

@author: rominasepulveda
"""

# Write a program that asks the user how many times he wants to print the letter X,
# and then prints a string with that number of X's

numXs=int(input('HOW MANY x?'))
toprint=''
iters=0
while iters<numXs:
	toprint="X"+ toprint
	iters+=1
print(toprint)
