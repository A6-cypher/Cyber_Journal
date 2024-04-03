#Data Structure in python(Collection of data)

myvalues=[3,3,4,'cypher']

#Built in data structures(List, tuple, dictionary, set)

#Data Structure: Lists

my_list=[]
my_list1=[3,1,2,"python",3.1]

bool(my_list)  #False(empty list ==> false)

print(my_list1[3]) #assesing python list
print(my_list1[3][1]) #assesing index values

print(my_list1[1:]) #using [:] to find a range inside a list

print(my_list1.index(3.1)) #searching in a list(Giving the column number)

my_list1.append("Python1") #adding to the end of the list

#Data Strucuture: Tuple

my_tuple=()
my_tuple1=(1,2,3,12.1,2)

print(my_tuple1)

bool(my_tuple) #==> false
bool(my_tuple1) #==> true

#tuple and strings are immutable

print(my_tuple1[1:]) #using [:] to find a range inside a list

#Data Structure: Dictionary
#Define Dicitonary

my_dict={'Fruit':'apple','animal':'fox',1:'one'}   #first is key, second is value{key,value}

print(my_dict)
print(my_dict['Fruit'])
print(my_dict.get('animal'))  #find the value based on keys

my_dict['three']=3 #adding to the dictionary

#Data structure: Sets

my_set={3,21,21,3,45,67,85,42}
print(my_set)
















