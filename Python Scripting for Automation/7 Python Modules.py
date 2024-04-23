'''
import math
print(math.pi) ==> 3.142.....
dir(math) ==> list of functions
help(math) ==> Documentations



Types of Modules

Default
Third party

use pip to install third party modules
pip install boto3

----------------------

2nd way

from math import *
print(pi)
print(pow(3,2))




'''

#Platform Module

import platform
#help(platform)
print(platform.system())
print(platform.python_version())
print(platform.machine())
print(platform.platform())

#Getpass Module

import getpass

db_pass=getpass.getpass(prompt="Enter your database password: ") #==> provide good practice

print(db_pass)













