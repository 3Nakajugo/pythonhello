#!/usr/bin/python

list = [1,2,3,4,5]

for number in list:
    print (number)
    number = number*2
    print (number)
print ("bye")

for letter in "hello":
    print (letter)
print ("bye")

#sequence iterating 

for index in range(len(list)):
    print ("number:" ,  index  )
print ("bye")