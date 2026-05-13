#EXCEPTIONS

#An exception is runtime error ,Error occurring while program executes.

#eg
x = 10 / 0

#will show zero divisibility error

#Exception handling

#exception handling is important because an exception can disrupt and program and crash it
#exception should be handled carefully were error can be handled without crashing a program


try: #try block is where were risky code is placed
    x = 10 / 0
except ZeroDivisionError: #this is exception for zero divisibility errors
    print("Cannot divide")


#multiple blocks of exception
try:
    num = int(input())

except ValueError:
    print("Invalid number")

except TypeError:
    print("Wrong type")


#finally
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File missing")

finally:
    print("Closing resources") #finally run even if a error occurs


# flow structure

#try:
    #risky code

#except:
    #if error occurs

#else:
    #if no error

#finally:
    #always runs


#RAISE

#raise is used to create errors intentionally it is used for invalid input,security check fails etc

#eg
age = -5

if age < 0:
    raise ValueError("Invalid age")


#CUSTOM EXCEPTIONS

#this is used to create custom exceptions of any type to meet needs for a system

#eg
class InvalidAge(Exception): #here Exception is used to inherit base Exception class
    pass

age2 = -1

if age2 < 0:
    raise InvalidAge("Age cannot be negative")



#HIERACHY FOR MULTIPLE EXCEPTIONS
#Exception
 #├── ValueError
 #├── TypeError
 #├── IndexError
 #└── FileNotFoundError

