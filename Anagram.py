# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 11:41:08 2022

@author: Adagani
"""

str1 = input("Enter the First String  = ")
str2 = input("Enter the Second String = ")

if(sorted(str1) == sorted(str2)):
    print("Two Strings are Anagrams.")
else:
    print("Two Strings are not Anagrams.")