name = "Tony Stark";

# example - if we want to comver given string  to iupper case - we can use the method upper()
# this upper() method will not change the original string but returns a new string which is same as previous string but converted to upper case

print(name.upper());
print(name);


# to find the position of character/string in a string, we use a method find(argument) and pass the character as argument, and it will return the index of that character/string
# if found it will return the index postion, if not, it will return -1

print(name.find('S'));
print(name.find('f'));
print(name.find('Stark'));


# to find a character or string in a variable we use 'in' KEYWORD
# answer will be 'True' in this case
print('T' in name);

# answer will be 'False' in this case
print('F' in name);

