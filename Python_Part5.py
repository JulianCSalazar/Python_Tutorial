# Classes are a manually created data type, much like ints, strings, and lists.
#   The key difference now is you get to decide what makes up your data type.
# An instance is a unique use of your new data type. So, if you were to make a
#   person class that required name, age, and eye color fields; Julian would be
#   an instance (that's me!) with my name being Julian, my age being 23, and my
#   eye color being 23. If I were to classify another person, that would be a
#   new instance.

class Name:
    def __init__(self, fn=None, ln=None):
        self.firstname = fn
        self.lastname = ln

class Person:
    def __init__(self, fn=None, ln=None, ec=None, age=-1):
        #Person's default values
        self.name = Name(fn, ln)
        self.eyecolor = ec
        self.age = age
        
class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
        
    def getBalance(self):
        self.log("Balance checked: " + str(self.balance))
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.log("+" + str(amount) + " : " + str(self.balance))
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.log("-" + str(amount) + " : " + str(self.balance))
        
    def log(self, message):
        myLog = open(self.name+".txt", "a")
        print(message, file = myLog)
        myLog.close()

its_me = Person()
try:
    print(its_me.name.firstname)
except:
    print("Your name isn't printable")
    
its_me.name.firstname = "Julian"
its_me.name.lastname = "Salazar"

try:
    print(its_me.name.firstname)
    print(its_me.name.lastname)
except:
    print("You broke your name!")
    
its_someone_else = Person()
its_someone_else.name.firstname = "Florence"
its_someone_else.name.lastname = "Welch"

try:
    print(its_someone_else.name.firstname)
    print(its_someone_else.name.lastname)
except:
    print("You broke someone else's name!")
    
# A method is a function declared within a class
#   They functionally work the same as functions
    
# Constructors are common types of methods used in classes that run when
#   a new instance of the class is created. They are usually named __init__()
# Destructors are another common method that destroy an instance
# Getters retrieves values held by the object
# Setters are methods that will change the values of the fields within the
#   instance

myBankAccount = BankAccount("Julian")
myBankAccount.deposit(500)
myBankAccount.withdraw(150)
print(myBankAccount.getBalance())

# Objects are mutable. So, you must be careful when making copies of instances.
#   You have to copy them at their immutable levels. See an example below.

# In this example, two variable are referring to the variables, so changing one
#   changes both.
#mySecondAccount = myBankAccount
#mySecondAccount.deposit(200)
#print(myBankAccount.getBalance())
#print(mySecondAccount.getBalance())

# In this example, we successfully copy our original account but now the copy
#   acts as its own unique account, so they don't refer to the same things that
#   the original account does.
mySecondAccount = BankAccount(myBankAccount.name, myBankAccount.balance)
mySecondAccount.deposit(200)
print(myBankAccount.getBalance())
print(mySecondAccount.getBalance())