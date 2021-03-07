#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name']) #values are accessed using keys

dict1 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}

print(str(dict)) # creates a string rep of the dictionary

print(type(dict)) # returns trype of object

dict.clear()#removes alll items from dictionay
print(dict)

print(dict1.copy()) #creates a copy of the dict

sequence = ('name', 'age', 'sex')
dict = dict.fromkeys(sequence) #creates dict with no values
print(dict)

dict = dict.fromkeys(sequence, 23) #creates dict with values
print(dict)

print(dict.get("name")) #gets object using its key

# print (dict.has_key("name")) #returns true is key exists, throews error

print(dict1.items()) #returns dict objects in list of tuples

print(dict1.keys())  # all keys in the dict

print(dict1.values())  # all vslues in the dict

dict.update(dict1) #adds dict 1 in key vslue pairs
print (dict) 

# dict.setdefault(key, default=None) # similar to get()
print(dict1.setdefault('firstname', None))
