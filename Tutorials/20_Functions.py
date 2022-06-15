# 3 types of fucntion
# inbuilt function
int()
str()
# module fiucntion
# --when same type of function is stored at one place Eg: Math Module
# ----module can be acccessed by "import Math"
# ------if we want to see all fucntions, it can be seen by print(dir(math))
# ----------if we want to import only sqrt fucnion from math module, we write "from math import sqrt"
# ----------if we want to import all, we write "from math import *"


# user defined fucntion

# Syntax
# def fucntion_name(parameters):
    # do something

def sum(first, second):
    print(first + second)

sum( 1, 2);

# in ccase no value is passed in the argument while calling the fucntion,  we can give default value to the parameters, 

def sum(first, second=4):
    print(first, second)

sum(1);