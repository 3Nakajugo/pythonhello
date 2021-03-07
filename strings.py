#!/isr/bin/python

#strings can be accesses using index

name="nakajugo"
print(name[4])

#updating strings
print(name+" edna")

print(name[4] + "e")

# escaape characters
print ("my name \t is \n nakajugo \a ")
print("c:\\ edna")

#string operators
print(name +" edna")
print(name * 2)

if "x" not in name :
    print ("its not there")
print("am there")

#string format operators using %

print("my name is %s and am %d kgs"%("edna", 59))

print(r"c:\\ edna")
print(u"c:\\23445mlgJDFKFPWEOedna") #UNICODE, Normal strings in Python are stored internally as 8-bit ASCII

# STRING METHODS
print(name.capitalize() )#string with first latter capitalised
print(",".join(name)) #takes a sequence in which dtring should be joined
print (name.upper())
# islower()
print(name.isdigit())
print(name.split(" "))
print(name.count("a"))#counts how many tiones character or string appears
# isdecimal
print(len(name))# returns length
isupper()#returns true is sting contains on upper case character
