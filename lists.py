#!/usr/bin/python

list1 = ['physics', 'edna', 19, 0] #can be accessed using index
list2 = ['physics', 'edna']
list3=[1,2,3,4,5,6,7]
t=(1,2,3,4)

#list methods

print(len(list1))
print(min(list2))
print(max(list2))
print(list(t))#converts seq to list
# print(cmp(list1, list2))

list2.append("edna1") #updating list
print(list2)

print(list3.count(1))#counts how many times an boject appears

list3.extend(list2)# merges two lists
print(list3)

print(list3.index(4)) # returns index of object

list3.insert(0, "new object")#inserts new object on specified index
print(list3)

print(list1.pop()) #returns last object in list

list3.remove(1) #searches and removes specified object
print(list3)
