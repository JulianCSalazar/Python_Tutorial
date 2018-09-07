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
# For a table use: \tab
# To display a " use: \"
# To display \ use: \\