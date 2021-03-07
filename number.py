#!/usr/bin/python

import math
#these are immutable data types, assigning a new values leads to creation of new object
var =1 
print(id(var))
print(id(var+1))#creates new object for var

print(type(var))
print(float(var))#change into float 

""" 
Mathematical functions
"""

#abs() , returns absolute positive value
print(abs(var))

#ceil(), smallest integer not less than x
number = 45.45
print(math.ceil(number))
print (math.sqrt(number)) #returns square root of number

#pow, return value of x to power y
print(math.pow(2, 3))

#floor largest number nt greater then x
print(math.floor(number))

"""
random number functions
"""
import random
#choice prints random item from list tuple or string
print("choice(['happy', 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("choice('String') : ", random.choice('String'))

#randrange prints radom element from given range




# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# def divisible_by_5():
numbers=[]
for number in range(2000,3000):
    if number%7==0 and number%5==1:
        numbers.append(str(number))
print(numbers)
# print (','.join(numbers))

# divisible_by_5()

        


