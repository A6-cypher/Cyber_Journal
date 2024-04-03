#Basic Operation on Strings

my_name = "Cypher"
my_ability = "trapwire"

my_info = """I am a character in Valorant. I am a sentinel. 
I provide defensive utilities for the team. 
I can be played offensive as well"""

#Using triple double quote to keep the format

print(f'my name is {my_name}\nMy ability is {my_ability}\nMy basic info: {my_info}')

#Slashing string into small parts

print(my_name)
print(my_name[0])
print(my_name[-1]) #last char

print(my_name[0:2]) # Slashing into first 2 char

#lenght of string

my_nameLenght = len(my_name)

print(f'lenght of my name: {my_nameLenght}')

#concatenate two strings

mystr = my_name+" "+my_ability
print(mystr)

#Case Conversion Operations

print(my_name.lower())
print(my_name.upper())

#use print(dir(string)) to get all operations for strings(case conversions)

#Boolean Result Operations(True or false)

print(my_name.startswith('c'))
print(my_name.endswith('er'))

print(my_name.islower())

#Join, center and zfill

x="python"
y="-".join(x)
print(y)

print(" ".join(y)) 

#mystrin.center(20), .center(20) it centers the string within 20 Char
#mystrin.zfill(10), it adds padding to the string

#Strip, split Operations

z=" Cypher       "
print(z)
print(z.strip()) #removes any spaces and give 

print(z.strip('y'))

print(z.strip('c').strip('r'))

#Count, index, find Operations

#x.count('p') counts number of p's
#x.find('p', 3) find the char/string as from the 3rd index(gives you -1 if not found)







