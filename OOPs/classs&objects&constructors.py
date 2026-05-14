#OOPS

#organizing code using objects for code reuse and many more
#Instead of writing everything as random functions and variables.
#each objects have data/properties and actions/behavior

#CLASS

#it is like a blueprint to make object
#this blueprint describe the structure ,design and features
#And an object is created based on this blueprint

class Student:
    pass



#OBJECT

#it is an instance of a class
#unlike class which is just a blueprint but not an actual thing
#object is an actual thing created using a class

s1 = Student()
s2 = Student()

#s1 & s2 are two separate object with separate memory

#objects can store data

s1.name = "Aravind" #this approach is not recommended cuz every object must be manually configured that is why constructor

s1.age = 20

#now s1 holds name and age data
print(s1.name)
print(s1.age)


#CONSTRUCTOR

#Constructor is special method automatically called when object is created
#it initializes object data and setup object state

#__init__ is the constructor method  in python

#eg
class StudentB:

    def __init__(self, name,age): #self  becomes----> object eg s1
        self.name = name
        self.age = age # self obtain the object when it is created i

    def greet(self):
        print( "hi",self.name)

s1.name = "Aravind" #attribute assignment self.name = name becomes --> s1.name = "Aravind" before constructor S1{} was empty

sA = StudentB(name="Aravind",age=20)
print(s2)


#SELF
#self represents current object

sB = StudentB("Aravind",20) # when sB is created python automatically calls   Student.__init__(sB, "Aravind",20)
                                       #s so self becomes sB
#self helps create many objects with different data and memory which can have same features and behavior


#METHODS
#methods are behavior which are in a class

print(sA.greet())#greet() is a method
                #internally python does this --> Student.greet(sA) where self becomes sA


#ATTRIBUTES
#attributes are data in a class

#eg
print(sA.name) #name is a data










