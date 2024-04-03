#Operators


#Arithmetric and Assignment Operators(+ - * / % // **)

expotential = 3**2 #==> 9
remainder = 7%2 #==> 1(gives remainder)

#Assignment operators( += -= *= /= %=)

a=3
b=3

a+=b #==> a=a+b

#Comparison Operators(> < >= <= == !=)

3>4 #==> False

3>4 #==> True

#Membership operator

valid_java=['1.6','1.7','1.8','1.9']
host_java='1.7'

if host_java in valid_java:                         #membership operator in and not in
    print('Host deployed with valid java version')
else:
    print("Host deployed with invalid java version")
    
    
#logical Operators(and or not)

print(3>1 and 1 in [2,3,4]) #==> false

print(2<3 and 4<6 and 6>1  and 7<10) #==> True
all([2<3,4<6,6>1,7<10]) #==>True all==and
any([2<3,4<6,6>1,7>10]) #==>false any==or




