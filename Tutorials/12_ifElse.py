age = 9;

# in other langauges, we use {} to define block, but in python we use proper indentation as a block
if age >= 18:
    print("you are an adult");
    print("you can vote");

# insteadd of else-if in other languages, we use elif
elif age < 18 and age > 3:
    print("you are in school");

else:
    print("you are just born");