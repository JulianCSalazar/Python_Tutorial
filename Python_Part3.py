#############################################################
# File : Python_Part3.py
# Author: Julian Salazar
# Date: 9/6/18
# Description:
#   This file is the sequel to the Python_Part2.py file and will contain
#   subjects covered in the third installment of my python courses. This file
#   will be a testing platform for Data Structure
# Contents:
#   1. Data Structures (Intro)
#   2. Strings
# Notes:
#
#############################################################

#############################################################
# DATA STRUCTURES
#############################################################
print("THIS BEGINS THE DATA STRUCTURES SECTION")

# PASSING BY VALUE VS. PASSING BY REFERENCE
# Passing By Value. When you pass an arguement to a function, even if you pass
#   a variable, the function will see it as a value or whatever value you made
#   your variable assume. The function will not see the actual variable though.
# Passing By Reference. When you pass a variable to a function, the function
#   can actually change the variables themselves instead of just using the
#   values they might hold.
# An example. If I pass by value a and b (where a = 1 and b = 2) into a 
#   function that adds them together and stores the result back in a, then it
#   will do the computation and store it locally within the function. However, 
#   when I check back on a after my function call, a is still 5. Why? Because,
#   when the value was passed by value, it can't change my variable.
# In python, integers are passed by value, but some languages, like C, allow
#   you to choose.

# The following code is an example of how python passes by value, at least for
#   primitive types. It will pass an integer into a function and print output
#   and show that the variable I passed in was unaffected.
def increment(an_int):
    an_int = an_int + 1
    print("an_int is:", an_int)
    
my_int = 2
print("my_int started as:", my_int)
increment(my_int)
print("my_int is now:", my_int)

# Python will effectively (but maybe not realistically) pass anything less 
#   complicated than a list (including string) as a value. Lists and above 
#   though will effectively be passed by reference.

# An interesting example of this concept and use of value vs reference can come
#   from variable assignment. The code below essentially performs the same
#   functions on an integer and on a list. Our output will show us how python
#   treats them differently.
a = 1
b = a
a = 83
print("a is:", a)
print("b is:", b)

list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print("list1:", list1)
print("list2:", list2)

# MUTABLE VS. IMMUTABLE
# A mutable variable is one that can change after it has been declared
# An immutable variable is one that can't change after it has been declared

# So are variables mutable or immutable. Are they passed by reference or value.
#   Realitically, everything in python is passed by reference and things like
#   integers are immutable. The code below will assigns the same variable one
#   value and the next line seemingly changes it, rendering it mutable, right?
#   Wrong. The variable points to an area in memory holding the first value,
#   when we call the variable again, instead of changing the value, it changes
#   the area in memory to a place that hold the new value.
# my_int points to a location in memory that holds the value 1
my_int = 1
# my_int points to a new location in memory that holds the value 2
my_int = 2
print("my_int:", my_int)

# Printing memory addresses is useful for deciphering whether or not a data
#   data type is mutable or immutable. In this first example, we show the int
#   is immutable since it needs to change addresses to change values.
my_int = 1
print("The memory address of my_int is:", id(my_int))
my_int = 2
print("The memory address of my_int is now:", id(my_int))
# This example shows that this data type is mutable since it's values change,
#   but its address doesn't.
list1 = [1, 2, 3]
print("The memory address of list1 is:", id(list1))
list1.append(4)
print("The memory address of list1 is now:", id(list1))

# In the case of integers and other less complicated types, the integers will
#   assume the same memory address if they share the same value. However, more
#   complicated types use different addresses even if the data they share is
#   identical. If you think about it, this dictates whether these types are
#   mutable or immutable, depending on if they act like they are passed by
#   value or reference.

# METHODS VS FUNCTIONS
# We have seen functions so far, and know how they work. We call them before
#   the main functions or where we call them and operate at the top levels of
#   our programs.
# Methods on the other hand operate specifically on data types to change them,
#   or perform some function on them. This is why they are tied to a variable
#   separated by period. Ex: list1.append() is a method.

#############################################################
# STRINGS
#############################################################
print(" ")
print("THIS BEGINS THE STRINGS SECTION")

# Three ways to define strings

# Establishing string with quotation marks
my_string = "12345"
print(my_string)
# Establishing string with apostraphes
my_string = '"12345"'
print(my_string)
# Establishing string with three consecutive apostraphes
my_string = '''"12345"'''
print(my_string)

# For a line break use: \n
# For a tab use: \tab
# To display a " use: \"
# To display \ use: \\

# The "in" operator returns booleans after determining a string is in fact held
#   within another string. Below are a couple of edge cases.
# The "find" method will tell you what index your string is FIRST found within 
#   the searched string. If it wasn't found, then it return -1.
my_string = "banana's"
my_empty_string = ""
try:
    if 0 in my_string:
        print("The 0 was found in the string")
    else:
        print("The 0 was not found in the string")
    print(my_string.find(0))
except:
    print("This 'in' operator is angry because I didn't give a string")
    
try:
    if "" in my_string:
        print('The "" was found in the string')
    else:
        print('The "" was not found in the string')
    print(my_string.find(""))
except:
    print("The in operator is angry because my string is empty")

try:
    if "b" in my_empty_string:
        print('The "b" was found in the string')
    else:
        print('The "b" was not found in the string')
    print(my_empty_string.find("b"))
except:
    print("The in operator is angry because my search string is empty")
    
# The "find" method actually is more powerful than the last example shows.
#   There are ways to use it that will find every instance of a string within
#   searched string. The way to do this is to take advantage of it's two
#   additional parameters which act as a start and end index to look within
#   the searched string.
searched_string = "asdfasdfasdfasdfasdfasdfasdfasdfasdf"
desired_string = "as"
i = searched_string.find(desired_string)
while i > -1:
    print("My desired string was found at", i)
    # Pushes the start search location past the last instance it was found
    i = searched_string.find(desired_string, i+1)

# Now before you go on thinking, "Wow! this would be a great way to count the
#   number of times my string is found", well there already is a method for
#   that. It is the "count" method. Just like the "find" method you can also
#   give a start and end point to look.
    
# Strings already have a ton of useful methods that can be used in fact. There
#   are several that are listed out below here to show some examples.
my_string = "this here is my FAVORITE string. "
print(my_string)
# Captializes the first character in the string
print(my_string.capitalize())
# Gives string with all lower case
print(my_string.lower())
# Gives string with all upper case
print(my_string.upper())
# Capitalizes every character that comes after a space
print(my_string.title())
# Removes white space from the start and end of a string
print(my_string.strip(" "))
# This replaces a string with another string
print(my_string.replace("this here", "that there"))
# This will separate the string into a list of string given a specified
#   delimiter. An interesting detail of this method is if you leave the
#   parameter field empty, it will automatically split by white space and
#   doesn't return any empty strings in the list it returns.
print(my_string.split(" "))
# This is pretty much the opposite of the split method, and will replace the
#   delimiter with a specified character.
print("-".join(my_string.split(" ")))

#############################################################
# TUPLES AND LISTS
#############################################################
print(" ")
print("THIS BEGINS THE TUPLES AND LISTS SECTION")

# Tuples are a list like data structure in python. The big difference between
#   the two though is that tuples are immutable and lists are mutable.

my_first_tuple = (1, 2, 3)
print("My first tuple is: ", my_first_tuple)

# Tuples are not restricted in any way to holding a single data type. If you so
#   desired you have a string, a float, and an int be held in a single tuple.
# But what if you need a single piece of data from the tuple. Well refering to
#   a tuple index is the same as a list or string.
print("The value in the second index of my tuple is:", my_first_tuple[1])

# This is about the extent of the usefulness of tuples. From here on, we will
#   use lists. Lists are structured and referred to similarly to tuples.

# Notice the big difference in structure here is that lists are made using
#   brackets
my_first_list = [9, 5, 3, 8, 7, 1, 6, 2, 4]

# Here is a nice long list of things we can do with our list. Note that, unlike
#   strings, the values of our original list variable will changes. With
#   strings, it required you to set the value of your editted string to the
#   original strings.
print("My first list is: ", my_first_list)
my_first_list.sort()
print("My list is sorted now as:", my_first_list)
my_first_list.append(0)
print("My list has a new appended value:", my_first_list)
my_second_list = [10, 11, 12, 13]
my_first_list.extend(my_second_list)
print("My list has appended another list:", my_first_list)
my_first_list.insert(1, -22)
print("My list has a new value added into index 1:", my_first_list)
my_first_list.remove(-22)
print("My list has had the value -22 removed:", my_first_list)
my_first_list.sort()
print("My first list sorted again:", my_first_list)
my_first_list.reverse()
print("My list sorted in descending order:", my_first_list)
print("My list has popped the value:", my_first_list.pop())
print("My list after the pop is:", my_first_list)
del my_first_list[-5:]
print("My list after deleting the last five items:", my_first_list)

my_2d_list = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

# A simple iteration of 2D list that will average the values of each sublist.
for sublist in my_2d_list:
    list_avg = 0
    for elem in sublist:
        list_avg = list_avg + elem
    print(float(list_avg)/len(sublist))

#############################################################
# FILES AND FILE TYPES
#############################################################

# Files must be opened and closed within our program. While the file is open
#  no other process can open and edit it. Because of this, we have to be clear
#  about closing it in our program so that other processes can open it when we
#  are done.

# Working with files can be a little finicky at times, so it is a good idea to
#  put your code into try blocks in case the process of opening your file
#  fails.

# When working with files, there are 3 main processes we can perform: reading,
#  writing, and appending. Reading allows us to view the file's contents.
#  Writing means we are going to start writing to a file from scratch. In
#  writing mode, it can be very easy to overwrite existing data. Appending is
#  like writing except you can only begin writing from the end of the file;
#  nothing is overwritten.

a = 12
b = 24
c = 46
my_list = ["Abigail Adams", "Stephanie Salazar", "Howl Jenkins", '\n']

# By default, python will look in the file path that this code is run to create
#  and search for new files.
# The open function opens our file. It has a optional second parameter aside
#  from our files name that will take the string "w"=write, "a"=append, and
#  "r"=read.
output_file = open("OutputFile.txt", "w")
#output_file = open("OutputFile.txt", "a")

# When we write to a file, we must write to it using a string format.
output_file.write(str(a) + '\n')
output_file.write(str(b) + '\n')
output_file.write(str(c) + '\n')
# The writelines() function will write individual elements of a list to a file.
#  However, it won't write on a new line, but we can get around that with the
#  join() function.
output_file.writelines("\n".join(my_list))

# The write() method isn't the only way to write to a file. The print function
#  can do it too actually. Print() uses a keyword parameter to assume that you
#  want your output to go to the console. We can change that though by giving
#  our file name.
for name in my_list:
    print(name, file = output_file)


output_file.close()