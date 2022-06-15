# list is a data type whcih is collection of primitive data types
marks = [95, 98, 97];
print( marks );

# to print for specific index, we use, variable_name[index]
print(marks[2]);

# if we pass value more than the maximum index, it will give output, "list index out of range"

# Negative index also exist in pyton, if we give negative index, python will start counting it from the back, for example,
# index -1 : 97
# index -2 : 98
# index -3 : 95
print(marks[-2]);


# to get range of numbers from the 
# we use colon, variable_name[starting_index : ending_index]
# the value at position of ending_index will not be included in the output
# for example if we give marks[0:2] then, value at position 2 will not be included in the output, instead value at position at index 0 and 1 will be displayed
print(marks[0 : 2]);


# for printing it individually
print("printing the values of list in sequence using for loop")
for score in marks:
    print(score);

# to add another value to the maarks we use append fucntion
print("Adding one more value to marks");
marks.append(99);
for score in marks:
    print(score);

# to add a value to the list, at any particular position using .insert(index, value)
print("adding value to the marks at particular position")
marks.insert(0, 100);
for score in marks:
    print(score);

# if we want to check , wheather a value exist in the list or not, we will take help of in keyword
# if pressent, it will generate output TRUE otherwise FALSE
print("checking the existence of 99 in list");
print(99 in marks);

# to get the length of the list we use len(variable_name) function
print("the length of the list is")
print(len(marks));

# to access the values in marks using while loop
print("accessing the values in list using while loop");
i = 0;
while i < len(marks):
    print(marks[i]);
    i += 1;

# to clear all the values inside list
marks.clear();
print(marks);