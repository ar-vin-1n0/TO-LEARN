#INHERITANCE

#inheritance helps to reuse properties and methods of another class
#core idea is child class inherits from parent class

#parent class --->super class / base class
#child class ---->derived class/ sub class


#without inheritance
class DogA:

    def eat(self):
        print("Eating")

class CatA:

    def eat(self):
        print("Eating")           #same code repeated

#Bad design
#code duplication
#harder to maintain
#can create system bugs


#with inheritance
class Animal:

    def eat(self):
        print("Eating")


class DogB(Animal):     #now dog class has inherited animal class

    def bark(self):     #these are child specific methods created inside a child class which doesnt have anything to do with parent class animal
        print("Barking")


class CatB(Animal):     #now cat class has inherited animal class

    def meow(self):     #these are child specific methods created inside a child class which doesnt have anything to do with parent class animal
        print("Meowing")


d1 = DogA()
d1.eat()
d1.bark()

c1= CatB()
c1.eat()
c1.meow()

#python search eat() method in dog /cat class but it doesnt find one so it searches the parent class which is animal and finds eat() method and executes it


#single inheritance is what show above where 1 parent exits dog and cat inherites from animal


#multilevel inheritance - chain inheritance
class AnimalS:
    pass

class Mammals(Animal):
    pass

class Dogs(Mammal):
    pass

#dogs inherites methods and data from both animal and mammals and mammals inherites from animals creating a chain


#Multiple inheritance

#Child inherits from multiple parents.
class A:
    pass

class B:
    pass

class C(A, B):
    pass

#here class c inherites from a and b



#Super()
#Suppose parent constructor already initializes data Without super(), child would need to rewrite logic.

#eg
class AnimalA:

    def __init__(self, name):
        self.name = name

#without super()
class Dogb(Animal):

    def __init__(self, name):

        self.name = name        #child class unnecssarily intialises parent logic again
                                #bad design
#with super()
class Dogc(Animal):

    def __init__(self, name):   #just calls and resues parent constructor into child without rewritting it
        super().__init__(name)



#Method Overriding

#Child replaces parent behavior.

#eg
class AnimalB:

    def sound(self):         #animal provides a sound methods
        print("Animal sound")


class Dog2(Animal):

    def sound(self):         #dog has its own sound methods
        print("Bark")


d = Dog()

d.sound()   #dog sound method will ber used first

#because python search for a method first in the child class and if its not found then only it searches for parent class
#here sound is found in child and executes it so no need to look into parent

