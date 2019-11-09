# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:42:52 2019

@author: talam
"""

print("Welcome to Chip's Fast Food Emporium")

burger = int(input('Please enter a burger choice: '))
burger_menu = ['filler', 461, 431, 420, 0]

side = int(input('Please enter a side choice: '))
side_menu = ['filler', 100, 57, 70, 0]

drink = int(input('Please enter a drink choice: '))
drink_menu = ['filler', 130, 160, 118, 0]

dessert = int(input('Please enter a dessert choice: '))
dessert_menu = ['filler', 167, 266, 75, 0]

total = burger_menu[burger] + side_menu[side] + drink_menu[drink] + dessert_menu[dessert]

print('Your total calorie count is', total)