#Tuples

a = (10,20)

#immutabled
#hashable
#faster than lists

d = {
    (1,2): "point"
}
#can be used as keys unlike list because of immutability

#packing and unpacking

#it can pack mutiple values and unpack them by extracting

person = ("Aravind", 21)

name,age = person

#name = "Aravind",age = 21


#SETS

#unique
#mutable
#used to check membership in a very fast way
#.add to add and .remove to remove elements

b = set()
b.add(person)
b.remove(person)

c = set()

#union (b|c)
print(b|c)

#intersection (b&c)
print(b&c)

#difference
print(b-c)


#DICTIONARY

#key value pairs

student = {
    "name": "Aravind",
    "age": 21
}

#access value using key
print(student["name"])
print(student["age"])

#add new key and value
student["city"] = "TVM"

#modify value
student["age"] = 20

#remove
del student["city"]

#looping through dictionary
for key, value in student.items():
    print(key, value)

#dictionary complexity = O(1) because of the use of key value pairs

#nested dictionaries

data = {
    "user": {
        "name": "Aravind",
        "age": 21
    }
}

print(data["user"]["name"])


#STRING

name = "aravind"

#sequence of characters

#indexing
print(name[3])

#slicing
print(name[1:4])

#split()

#converts string into lists
print(name.split(","))


#join()

#converts list into string
result = "".join(name)
print(result)


#replace()

#replace a string with another
print(name.replace(" ", "_"))


#strip()

#removes space from a string

#find()

#find a string inside a string and returns its index if it is in the string


#how add items in a string like since string is immutable

chars = []

for c in name:
    chars.append(c)

result = "".join(chars)
print(result)


#frequency counting string

freq = {}

for char in name:
    freq[char] = freq.get(char, 0) + 1

print(freq)