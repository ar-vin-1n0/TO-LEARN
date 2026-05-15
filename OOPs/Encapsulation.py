#ENCAPSULATION

#bundling data and methods together
#restricting direct access to internal details

#eg

#without encapsulation
class BankAccount:

    def __init__(self, balance):
        self.balance = balance


account1 = BankAccount(100)

account1.balance = -200  #real bad here account balance goes to a minus it becomes invalid

print(account1.balance)

#this design is bad because it can be modified ,systems should protect critical information

#with Encapsulation

#using encapsulation we can hide internal data and only give access to needed information only by providing controlled methods

class BankAccountA:

    def __init__(self, balance):
        self.__balance = balance        #double underscore meaning private attribute python hides it from direct access

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount  #if balance becomes negative it shows error it will only go till 0

    def get_balance(self):
        return self.__balance

accountB = BankAccountA(100)

accountB.deposit(100)       #these are controlled methods where access is controlled

print(accountB.get_balance())

#direct attempt to tamper
accountB.__balance = + 11100

print(accountB.get_balance())  #balance doesnt get tampered

        #Outside Code
        #     ↓
        #Controlled methods
        #     ↓
        #Validation
        #     ↓
        #Internal data


#getters and setters

#getters
#getters are used to read private data

#eg
accountB.get_balance()  #get_balance is a getter which returns the balance info which is private


#setters
#setter are used to modify private data safely using validation,logging,restriction

#eg

accountB.deposit(100)  #.deposit method is a setter where it modifies the balance data which is private in a controlled and safe way


#@property - used to turn a method into an attribute-like property

class Student:
    def __init__(self, marks):
        self._marks = marks    #use _ ,_mark to make it internal and private

    @property
    def marks(self):
        return self._marks

    @marks.setter           #used for modifying safely and with validation and restrictions
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks")
        else:
            self._marks = value

    @marks.deleter         #used to delete a value from a private method like marks by safe and controlled deletion
    def marks(self, value):
        if value < 0 or value > 100:
            del self._marks



s = Student(95)

print(s.marks) #s.mark not s.mark() methods behave like variables

s.marks = 95
print(s.marks)

s.marks = 150  #this will show invalid marks

print(s.marks)








