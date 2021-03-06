#!/usr/bin/python

# assign variable

count = 0
name = "edna"
last = "nakajugo"

print (name + last)

# multiple assignment 
a=b=c=1
print (a)
print (b)
print (c)

#python numbers
var1 =1 
var2 =2

del var1 #delete avriable

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'var1' is not defined

#python strings
str ="nakajugo edna"

print(str[4]) #prints 4th index
print (str[2:7]) #print fron 2 index to 7th
print (str * 2)
#nakajugo ednanakajugo edna
print (str + 'wwww')
#nakajugo ednawwww

#python lists
names=["edna", "mary", 2, 2.1, "sam"]  
secondname=["happy", "exicted"]
print(names) #prints whole list
#['edna', 'mary', 2, 2.1, 'sam']
print(names + secondname)#concatinates two lists 
#['edna', 'mary', 2, 2.1, 'sam', 'happy', 'exicted']
print(names[-1]) #prints last digit in list
#sam
print(names[2:]) #prints fron second index to last
#[2, 2.1, 'sam']
names[0]="nakajugo" #updates item at index 0
print (names) 
#['nakajugo', 'mary', 2, 2.1, 'sam']

#python tuples
tuple =("edna", "mary", 2, 2.1, "sam")
secondtuple=("happy", "exicted") 
# tuple[2] = 1000 updating a tuple is nor possible
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

#python  dictionary
dict['one']= "onne" 
print(dict['one'])# access dict values using keys
# print (dict.keys())
# dict_keys(['one'])
# >>> print (dict.values()) 
# dict_values(['onne'])

