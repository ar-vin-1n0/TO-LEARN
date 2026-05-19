#CONTEXT MANAGERS

#The MAIN purpose of context managers is safe resource management

#if you  file = open("data.txt")
#python and os allocates memory,file handles,system resources

#if file isn't closed resource exhaustion and memory leak happens

file = open("data.txt")

data = file.read()

print(data)

#Before context managers Python programmers used

#try:
#    ...
#finally:
#    ...

file = open("data.txt")

try:

    data = file.read()

finally:  #closes file even if an exception happens

    file.close()

#Open file
#   ↓
#Run code
#   ↓
#Exception happens
#   ↓
#finally still executes
#   ↓
#file.close()

#Problem with try/finally Everywhere
#This works,
#BUT becomes:
#repetitive
#ugly
#error-prone
#Large systems would contain endless cleanup code


#Context managers AUTOMATE setup + cleanup

#with statement
#syntax -- with something as variable:

with open("data.txt") as file:  #closes file automatically

    dataA = file.read()  #give file object

    print(data)


#ENTER context
#↓
#resource acquired
#↓
#code executes
#↓
#EXIT context
#↓
#resource cleaned automatically


#with open("data.txt") as file:
#     ↓
#internally behave like:
#     ↓

#file = open("data.txt")

#try:

# block code

#finally:

#    file.close()


#Context managers are elegant automation of try/finally


#Context Manager Protocol

#must implement
#Method	        Purpose
#__enter__()   	setup/start
#__exit__()	    cleanup/end

#enter() -- Called automatically when entering context
#exit() --  Called automatically when leaving context


#Custom context managers

class MyContext:

    def __enter__(self):
        print("Entering context")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")


with MyContext() as obj:  #object created

    print("Inside block")


#Exception Handling in Context Managers
class Test:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Error handled")


with Test():
    x = 10 / 0

#Start
#Error handled      #__exit__() happens even if an exception happens

#def __exit__(self, exc_type, exc_value, traceback):   contain info about exception

#Parameter	Meaning
#exc_type	exception type
#exc_value	actual error
#traceback	stack trace


#Suppressing Exceptions

with Test():
    x = 10 / 0

print("Program continues")  #surppress the errors and continues program without crashing

#Context Managers with contextlib

from contextlib import contextmanager


#A module used for context managing


#Generator-Based Context Manager

@contextmanager
def my_context():
    print("Enter")

    yield

    print("Exit")


with my_context():
    print("Inside")

#before yield → __enter__
#after yield → __exit__

#In context managers:
#yield
#separates enter/exit logic.


#Why use context managers

#Benefit	           Meaning
#automatic cleanup	   safer systems
#exception safety	   fewer bugs
#cleaner syntax	       readable code
#resource management   professional design