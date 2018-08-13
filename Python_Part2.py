#############################################################
# File : Python_Part2.py
# Author: Julian Salazar
# Date: 8/4/18
# Description:
#   This file is the sequel to the PythonIntro.py file and will contain
#   subjects covered in the second installment of my python courses. This file
#   will be a testing platform for control flow code.
# Contents:
#   1. Conditionals
#   2. Loops
#   3. Functions
#   4. Exception Handling
#
# Notes:
#  Sometimes conditional statement can be fairly long (involving lots of ands 
#   and ors) so if a line needs to be broken up into multiple lines, you line
#   split with '\' at the end of each line.
#
#############################################################

#############################################################
# Conditionals
#############################################################
print("THIS BEGINS THE CONDITIONALS SECTION")

# Basic if-then example.
todays_weather = "Raining"
suggestion = "Nothing"

if todays_weather == "Raining":
    suggestion = "You should wear rain clothes today"
print("If-then statement response is:", suggestion)

# Basic if-then-else statement. Notice that the else statement only pairs with
#   the most immediate if statement in its scope. An if-then-else will ALWAYS
#   run one of the two blocks of code (unless it crashes for some reason). Play
#   with the value of todaysWeather to see it in action
todays_weather = "Sunny"
suggestion = "Nothing"

if todays_weather == "Raining":
    suggestion = "You should wear rain clothes today"
else:
    suggestion = "You should dress for dry weather"
print("If-then-else statement response is:", suggestion)

# If-then-else-if-else statement. This is similar to the previous two examples
#   but gets more specific and covers more cases. Again, it will enter only one
#   case from the entire block.
todays_weather = "Cold"
suggestion = "Nothing"

if todays_weather == "Hot":
    suggestion = "Wear a t-shirt"
elif todays_weather == "Cold":
    suggestion = "Wear a sweater"
elif todays_weather == "Raining":
    suggestion = "Wear a rain coat"
else:
    suggestion = "Prepare for anything"
print("If-then-else-if-else statement response is:", suggestion)

# Set membership operator example with list.
sweater_weather = ["cold", "raining", "windy"]
todays_weather = "cold"

if todays_weather in sweater_weather:
    print("Set membership example says wear a jacket")
else:
    print("Set membership examples says jacket is unnecessary")

# Nested conditional example. This example will check to see if I am able to
#   go to the movies depending on some criteria like cost and reviews
desired_movie = "Deadpool"
my_money = 30
movie_review = 4.2

available_movies = ["Deadpool", "Avengers", "It", "Inception"]
ticket_cost = 11
acceptable_review = 3.5

# Check to see if the movie we want to see is in theaters
if desired_movie in available_movies:
    # Checks to see if we have money to see a movie
    if my_money >= ticket_cost:
        # Checks to see if the movie we want to see got good reviews
        if movie_review >= acceptable_review:
            print("Go watch", desired_movie)
        # Runs if movie_review didn't meet our review criteria
        else:
            print("This movie didn't generally get good reviews")
    # Runs if you don't have enough money to see a movie
    else:
        print("You don't have enough money to see a movie")
# Runs if the movie you want to see isn't in theaters anymore
else:
    print("The movie you want to see isn't in theaters")
    
#############################################################
# Loops
#############################################################
print(" ")
print("THIS BEGINS THE LOOPS SECTION")


# Standard for loop prints every value in list given by range(1,11)
print("Start of first for loop")
for i in range(0,11):
    print(i)
print("End of first for loop")

# Python is more specialized for running operations on lists and uses for-each
#   loops for these purposes. It has the same format as our previous example,
#   and in fact, all for loops in python are for-each loops. This example is
#   the same as the one in PythonIntro.py
letter_count = 0
for character in "Hello World":
    letter_count+=1
print("The number of letters in 'Hello World' is:", letter_count)

# The following code serves the same purpose as the above code, but in a more
#   standard for loop setup
#my_string = "Hello World"
#letter_counter = 0
#for i in range(0, len(my_string)):
#    letter_counter += 1
#print("The number of letters in 'Hello World' is:", letter_counter)

# Standard while loop. Note that all for loops can be written as while loops,
#   so we will try and write the previous for loop as a while loop.
# The while loop continues to run so long as the conditional in its paranthesis
#   is true.
letter_count = 0
i = 0
my_string = "Hello World"
while(i < len(my_string)):
    letter_count += 1
    i += 1
print("The number of letters in 'Hello World' is:", letter_count)

# There are some keywords in python used with loops that change control flow.
#   These words are continue, pass, and break.
# Continue forces the current iteration of a loop to stop, skipping over
#   remaining loop code. It only corresponds to the innermost loop its called
#   in.
# Break is similar to continue, except it will completely exit the loop, where
#   continue skips back to the beginning of the loop.
# Pass is essentially no more than a blank indented line

#############################################################
# Functions
#############################################################
print(" ")
print("THIS BEGINS THE FUNCTIONS SECTION")

# Functions in python must be created before you use them, unlike in C where
#   you can make a prototype.

# The following function find the max value between two input parameters. In
#   this case the input parameters are op1 and op2. This function is an example
#   of a function that has both parameters and return values.
def Find_Max(op1, op2):
    if (op1 < op2):
        return op2
    elif (op2 < op1):
        return op1
    else:
        return None
    
print("Max(5, 7) is:", Find_Max(5,7))

# The following is an example of a function that has neither parameters or a
#   return value.
def Print_Hello_World():
    print("Hello World")
    
Print_Hello_World()

# Keyword Parameters
# When we create a function, we typically assume the user will enter all the
#   proper parameters for the function to run. But sometimes, they don't. In
#   the case they do not, and we still want the function to run and default the
#   ignored parameter to something, we use keyword parameters. The following
#   function will serve the same as Find_Max() but can take in 0, 1, or 2
#   parameters.
# Note: Keyword parameters must come after normal parameters in their listing.
#   So, if I only made one parameter and one keyword parameter in a function
#   it would like like:
#   def Func(op1, op2 = "Something"):
def Find_Max_V2(op1 = None, op2 = None):
    if (op1 == None) and (op2 == None):
        return "The user entered no parameters"
    # The elif below is technically unnessary. If the user entered a single
    #   parameter, it would default to assume the value of op1. The only
    #   instance where op1 would be None is if the user entered no values.
    elif (op1 == None):
        return op2
    elif (op2 == None):
        return op1
    else:
        if (op1 < op2):
            return op2
        elif (op2 < op1):
            return op1
        else:
            return "The operands are equivalent"
        
print("Find_Max_V2() gives:", Find_Max_V2(5))

#############################################################
# Exception Handling
#############################################################
print(" ")
print("THIS BEGINS THE EXCEPTION HANDLING SECTION")

# The following code will attempt to convert a string into an integer, and then
#   print the integer. It will fail because the value I entered to the int()
#   function is not a number.
# This code is a try and catch example. It will try and run the code in the try
#   bloack and if it encounters any error within the try block, it will run the
#   code in the except, or catch, block.
myVal = "Hello World"
try:
    print("Converting myVal to an int...")
    myNum = int(myVal)
    print(myNum)
except:
    print("myVal was not a number")

# The following is a bit more complicated. In this case we will be using the
#   try-except-else-finally structure. Each will be described as we go.
myVal = 6
# The code will begin in the try block and run until it might encounter an
#   error.
try:
    print("Converting myVal to an int...")
    myNum = int(myVal)
# The except block only run if there was an error encountered in the try block
except:
    print("myVal was not a number")
# The else block is a continuation of the try block. The code only jumps here
#   if the try block runs successfully. This block is more stylistic. You could
#   just leave this code in the try block, but it might be easier to follow if
#   we end the try block at the point in the code where we would expect the
#   error to occur.
else:
    print(myNum)
# The finally block runs no matter what, despite whether any error was
#   encountered or not. This block is more of a formatting and stylistic
#   feature. Often, we could leave the finally block off and put the code
#   in this block outside the scope of the exception handling code and
#   experience no repurcussion.
finally:
    print("Done!")