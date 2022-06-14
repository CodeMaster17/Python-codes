# question will be asked by the computer - "what is your name?" and it will be stored in the variable name
name = input("what is your name?")
# ooncatenaation- have to add extra space
print(name + " is a genuis");

#everything taken as input in python, python stores it as a string, wheeather it is a number or anything
# to convert the entered number which is in the form of string, to a number, we use a fucntion int(variable_name)

old_age = input("what is your age?");
# the line below will convert the the number in the form of string to a integer format and then add the 20 to it

new_age =  int(old_age) + 20;
print(new_age);

# other type converssion available in python are
# float()
# str() -- to convert to string
# bool() -- to convert to boolean