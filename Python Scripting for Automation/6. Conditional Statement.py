'''
if expression:
    statement1
    statement1


comparision operators ==> create expressions

'''

usr_str=input("Enter your string: ")
#usr_cnf=input("Do you want your string to convert into lower case?(yes or no): ")

'''if usr_cnf=="yes":
    print(usr_str.lower())
'''

#if elseif elseif elseif else statements

usr_cnf=input("Do you want your string to convert into?(lower, title, capital): ")

if usr_cnf=="lower":
    print(usr_str.lower())
    
elif usr_cnf=="title":
    print(usr_str.title())
    
elif usr_cnf=="capital":
    print(usr_str.upper())
    
else:
    print(usr_str)

