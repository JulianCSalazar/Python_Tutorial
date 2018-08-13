#############################################################
# File : PythonIntro.py
# Author: Julian Salazar
# Date: 7/21/18
# Description:
#   This file is a testing platform for basic python commands
# Contents:
#   1. Print Statements
#   2. Variables and Types
#   3. Logical Operators
#   4. Mathematical Operators
#
# Notes:
# >>Python is a dynamic scripting language rather than a static one like C.
#   The difference between the two is that dynamic languages don't need to be
#   compiled and static ones do. We can see this in action if we write an
#   incorrect instruction in Python and in C. The code will run all previous 
#   correct lines of code first before expressing there is an error once it
#   hits it. In C, however, the program will never run any lines because it
#   must compile first and is unable to do so because of the line with the
#   error.
#############################################################

#############################################################
# Print Statements
#############################################################
print("This begins output of Print Statements section.")
print("Bananas")
# Also try:
#print('Bananas')

# Each print statement puts the output on a new line. So the output of this
#   line with the previous line will give:
#   >>Bananas
#   >>Give them to me
print("Give them to me")

# The print statement will print, in a literal sense, anything in quotation
#   marks. However, it will print values without the quotation marks, as well
#   as boolean values. The last line (line 27) will give an error because the
#   boolean value is case sensitive and must be exactly 'True' or 'False'
print(5)
print(42.3)
print(True)
print(False)
#print(TRUE)

# The following prints multiple values and strings on the same line. Notice
#   that all the values are just comma separated. The output of this line gives
#   the output:
#   >>Why is 6 afraid of 7
print("Why is", 6, "afraid of", 7)


print(' ')
print("This begins output of the Variables and Types section.")
#############################################################
# Variables and Types
#############################################################
# Variables such as 'myNum' below can be used to store values and change
#   with different processes. Notice that it can also change data types as
#   needed. In this example it can change from an integer to a float and will
#   print:
#   >>myNum is 16
#   >>myNum is now 16.1
myNum = 16
print("myNum is", myNum, "and is of type", type(myNum))
myNum = 16.1
print("myNum is now", myNum, "and is of type", type(myNum))

# The variables myNum is created and initialized when we assign them
#   a value. However, it is possible to initialize a variable without assigning
#   it a value by setting the variable to 'None' which is Python's special word
#   for null.

# Some operators will only work on certain data types. For example it doesn't
#   make sense to multiply a string by 2.5. However, there are some funky
#   tricks. Try running the commented line in the series below:
myString = "Bananas"
myNum = 2.5
#print(myString*myNum)
# The line will give an error that species you can't multiply a non-int with
#   our string. So lets try an int:
myNum = 3
print("This is the result of multiplying a String and an Int: ",
      myString*myNum)
# The output in this case is going to be our string printed 3 times as:
#   >>BananasBananasBananas

# Booleans can also be mathematically operated on, and assume the values 1 for
#   'True' and 0 for 'False'.

# Play area:
d = print("Adding two strings together: ", "Hello" + "World")
print("The value of the output of a print statement is:", d)


# Type Casting
myNum = 5
print("I currently have value of", myNum, "that is type ", type(myNum))
# Above is some code that will print some info about the variable myNum. Next,
#   we will do the same thing but after some type casting. What the following
#   code will do is take our numeric value and translate it into text.
myNum = str(myNum)
print("I now have value of", myNum, "that is type ", type(myNum))
# Now we will play with casting different types to floats, ints, and bools
#   using the functions float(), int(), and bool().
print("TYPE CASTING")
# This line will cast a float to an int but in doing, we will lose all info
#   after the decimal. Printing this value will only give '5'.
print(int(5.1))
# This lines casts an int to a float. We make it into a decimal value and it
#   will print '5.0'
print(float(5))
# We can cast strings to floats and ints but only in particular circumstances.
#   The first few lines below will print successfully, but the
#   other lines will throw errors for different reasons. Check each out
#   individually to see exactly goes wrong.
print(int("5"))
print(float("5"))
print(bool(0.0))
print(int(False))
print(bool("0"))
print(bool(5.1))
#print(float("a"))
#print(int("5.1"))
#print(int("a"))
# It appears the bool() type caster will set any value to true unless it is the
#   the integer or float value 0.
# Try different strings at the command terminal to see if they can be casted
#   into these forms.
#v1 = input("See if this value can be casted from a string to an int: ")
#int(v1)
#print("SUCCESS!")
#v2 = input("See if this value can be casted from a string to a float: ")
#float(v2)
#print("SUCCESS!")
#v3 = input("See if this value can be casted from a string to a bool: ")
#bool(v3)
#print("SUCCESS!")


print(' ')
print("This begins output of the Logical Operators section.")
#############################################################
# Logical Operators
#############################################################
# Logical operators include:
#   >>'==' to check for equality
#   >>'>' to check for one value being greater than another
#   >>'<' to check for one value being less than another
#   >>'>=' to check for one value being greater than or equivalent to another
#   >>'<=' to check for one value being less than or equivalent to another
#   >>'and' is a boolean operator that does a bitwise and on your values
#   >>'or' is a boolean operator that does a bitwise or on your values
#   >>'not' is a boolean operator that is inverts a single values bits

# The following is some code using logical operators. The output of the code
#   will give boolean values for the relational operators and numeric values
#   for boolean ones.
a = 5
b = 4
c = 3
# This line will print the value 'True' since 5 is greater than 4
print("Result of a>b is: ", a>b)
# This line will print 'False' since 5 is not equivalent to 4
print("Result of a==b is: ", a==b)
# This will print the value '4'. Since 5 = 0b0101 and 4 = 0b0100, a bit wise
#   will leave only 0b0100. Typically the boolean operators will be used on
#   boolean values rather than integers. 'and' statements are only true if
#   both statements are true. 'or' statements are true if either statement is
#   true. 'not' statements would simply make a true into a false, and a false
#   into a true.
print("Result of a and b is: ", a and b)

# Relational operators can be operated on strings too, not just number values.
#   in the code below, we will illustrate some of the nuances of doing such
#   things.
string_1 = "dead"
string_2 = "beef"
# This statement will return false since dead and beef are not the same
print("Result of 'dead'=='beef' is:", string_1 == string_2)
# This statement will return true! The operator will compare the value of the
#   first letter of each word. Since 'd' is after 'b', it perceives it as 'd'
#   being greater than 'b'
print("Result of 'dead' > 'beef' is:", string_1 > string_2)
string_1 = "Dead"
# This statement will return False. Python interprets capital letters as being
#   less than lower case letters, no matter the letter.
print("Result of 'Dead' > 'beef' is:", string_1 > string_2)

# The 'in' set operator will check to see if a value or subset is contained
#   within a list or larger set. In this example we will just see if some
#   letters and words are in string.
string_1 = "This **** is bananas"
print("Checks to see if 'bananas' is in string_1:", "bananas" in string_1)
print("Checks to see if 'beef' is in string_1:", "beef" in string_1)
print("Checks to see if the letter 's' is in string_1:", "s" in string_1)

# Orders of operation. Python will usually run the 'and' statements first, and
#   then the 'or's. The statements belows should give the outputs True.
print(True or True and False)
print(True and False or True)


print(' ')
print("This begins output of the Mathematical Operators section.")
#############################################################
# Mathematical Operators
#############################################################
# There are four basic mathematical operators: '+', '-', '/', and '*'. Division
#   is the only math operator that doesn't maintain int types when ints are
#   involved. If we divide 2 ints, it will automatically make the result a
#   float, besides whether or not the ints evenly divide.
# There is a fifth operator python can often implement called modulus and is
#   represented as '%'. It takes two values and will give you a remainder. The
#   mod operator won't take in 'False' as its second value, and can't work on
#   strings.
print("The result of 6.5%4.2 is:", 6.5%4.2)
print("The result of 7%True is:", 7%True)
# In terms of order of operations. It will perform the mod like a mult or div.
print("The result of 1+3%2 is:", 1+3%2) #Notice it performs the mod first.

# There are some other operators in python. One of them is floor division,
#   given as '//'. Using this between any two values it will auto round down.
#   Another is the exponentiation operator, given as '**'.
print("The result of 4**2-1 is:", 4**2-1) # Performs the exp first
print("The result of 4**2**2 is:", 4**2**2) # Mults the exps together
print("The result of 4**2*2 is:", 4**2*2) # Performs the exp first
print("The result of 4*2**2 is:", 4*2**2) # Performs the exp first
# Floor operators receive the same priority as regular division

# Self-Incrementing. In line 237, we use a self incrementing operator. We can
#   actually replace the '+' with any math operator.
letterCount = 0
for character in "Hello World":
    letterCount+=1
print(letterCount)