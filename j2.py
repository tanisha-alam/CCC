# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:35:43 2019

@author: talam
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b < c < d:
    print('Fish Rising!')
elif a > b > c > d:
    print('Fish Diving!')
elif a == b == c == d:
    print('Fish at constant depth.')
else:
    print('No Fish.')