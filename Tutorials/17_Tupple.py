# tupple is same as lists but once created, tupple cannot be changed, for example it cannot be append, insert etc

marks = (95, 98, 97)
# the line below will be invalid
# marks[0] = 99

# tupple can count the frequency of its values
marks=(95, 98, 97, 97, 97)
# to count the frequency of a value we use count function .count(value)
print(marks.count(97))


# index of the element can be found out by using .index(value) of the function
print(marks.index(97));