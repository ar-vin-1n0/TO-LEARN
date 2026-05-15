#POLYMORPHISM

#Polymorphism helps to have same interface and have different behaviors

#for a same method each objects behave differently

#eg
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()          #theres going to be different behavior for the same behavior

#using polymorphism is simple and scalable


#without using polymorphism
if type(animal) == Dog:
    animal.bark()

elif type(animal) == Cat:
    animal.meow()

#bad design

#Polymorphism often happens through method overriding
#where child class methods happen without using parent class method which both are same


#method overloading

#unlike c and java
#python handle and does method overloading different

#same method name
#different parameters
#different behavior

#python uses default ,args and kwargs

#default args
class Calculator:

    def add(self, a, b, c=0):

        print(a + b + c)

#*args
class Calculator:

    def add(self, *nums):

        print(sum(nums))




