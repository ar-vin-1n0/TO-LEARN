# TIME COMPLEXITIES

# O(1)

# O(1) = run time remain same even if its 1 or its a million as input it always remains constant

   #example

n = [1,2,3,4,5]

print(n[1])
print(n[5])

#print(n[1000000])

    #all the 3 process take the exact time without being influenced by the size or amount of the input
    #append() in list also exhibits the same O(1) complexity


#O(n)

#O(n) = run time grows linear to the input operation it depends on the size and amount of input

    #example

for num in n:
    print(num)

    #if the number of elements in the list n is 10 it will take 10 operation to complete and if it is 1000 it will take 1000 operation
    #complexity grows linear to the input size


#O(n^2)

#O(n^2) = run times explodes very fast as the input size increases

    #example

for i in range(len(n)):
    for j in range(len(n)):
        print(n[i],n[j])


    #O(n^2) happens mostly in nested loops like if the len(n) is 100 then operation of 1st loop = 100 operation of the 2nd loop is 100 operation for every outer loop
    #that 100 * 100 = 10000 operations  ---> grows very fast for every increase in input size


#O(log n)

#O(log n) = very efficient used in divide and conquer methods eg :binary search

    #example

#binary search

# find 4 in list n

#while linear search may search every element in the ist with the searching element which is O(n) complexity
#binary search take middle element and check element for search eliminates half and repeats till result

#here take 3 checks eliminates left half repeats checks 4,5 takes middle 4 checks confirm found 4 at n[3]


#O(n log n)

#O(n log n) = is very fast used to be best sorting methods like merge sort / python sort()

    #example

#sorting   python sort()

n.sort()

#if it was bubble sort with O(n^2) if n = 100 than operations = 1000000
#but python sort with O(n log n) if n = 100 than operations = ~10000
#huge difference

#O(2^n)

#O(2^n) = most dangerous and demanding complexity it increases exponentially  with input size

    #example

#fibonacci recursion
#F(n) = F(n-1) + F(n-2)
#0, 1, 1, 2, 3, 5, 8, 13, 21


#HASH SET LOOKUP

#normal list lookup is  in O(n) complexity
#eg:
k = 4
if k in n:
    print(n)


#set lookup is in O(1) complexity
set_lookup = set(n)
if k in set_lookup:
    print(set_lookup)


#SPACE COMPLEXITY

#space complexity is about memory usage and its complexities

#eg:
print(n[::-2]) # creates a new list O(n) complexity

n.sort() # modifies the existing list O(1) complexity


