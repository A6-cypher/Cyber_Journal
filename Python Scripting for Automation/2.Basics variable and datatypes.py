#Classtype and Variables

x=4
print(x)

y=1.2

print(type(x))
print(type(y))

#delete a variable

del x

#Finding the id(memory of a variable)

a=4
print(id(a))

id_a = id(a)


#Different data types

g=2;h=2.2;p=3+3j

print(g,type(g))
print(h,type(h))
print(p,type(p))

lan_name= 'python scripting'
print(lan_name)

my_name= "X"
print(my_name,type(my_name))

my_value = True
my_new_value = False

print(my_value,type(my_value))

#Type Convertion

num=21
print(num,type(num))

num1=str(num)
print(num1,type(num1))

num3=bool(num)
print(num3,type(num3))

q=bool(0)
# print(q,type(q))

#any datatype can be converted into boolean
'''
bool(empty)=False bool(0) bool(None boool(())
bool(non-empty) = True

Any datatype can be converted into a string(Not in reverse)

'''

#Printing in certain formate or order

int1=1;int2=1.23;str1="abc"

# print(int1,int2,str1)

# print(("{}\n {}\n\t {}".format(int1,int2,str1)))

# print(("{} {} {}".format(str1,int2,int1)))

#use this better
print(f"Int1 value is {int1} \nInt2 value is {int2} \nStr1 value is {str1}")


#Now we are looking into input and output

#Simple Addition Cal

val=eval(input("Enter the first value: "))
val1=eval(input("Enter the second value: "))
result = val+val1

print(f"Your addition is {result}")

