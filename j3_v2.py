# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 09:01:32 2019

@author: talam
"""

# Indicates which block they are in after their roll
i = 1

# Keep rolling until you win the game
while i < 100:
    roll = int(input('Enter sum of dice: '))
# There are two dices, and their sum cannot be smaller than 2 or larger than 12
    if 2 <= roll <= 12:
# If the roll exceeds 100, the user has to roll again
        if i + roll > 100:
            print('Your number is too big, my lad. Roll again!')
# The roll is added with the block to update it
        else:
            i = i + roll
            print('You are now on square', i)
# How to quit the game
    elif roll == 0:
        print('You Quit!')
        i = 100
    else:
        print('Invalid roll. Please pick a number from 2 to 12.')
    
# The different snakes in the game and where you will be put once displaced
    snakes = {54: 19, 90: 48, 99: 77}
    if i in snakes:
        i = snakes[i]
        print('Oh no, you got eaten by a snake! Now you are at', i)

# The different ladders in the game and where you will be put once climbed
    ladders = {9: 34, 40: 64, 67: 86}
    if i in ladders:
        i = ladders[i]
        print('You climbed up a ladder! You go to', i)
        
# You Win!        
    if i == 100:
        if roll != 0:
            print('You Win!')