# 1: LIST
# create 2 lists of numbers
numList1 = [2,3,4,5,6]
numList2 = [5,7,8,4,12]
# type a function that takes a parameter
def add(numToAdd):
    print("Sum of all list numbers is",sum(numToAdd))
    
# call defination of function  with argument
add(numList1)     
# call function with another argument
add(numList2)   

# 2: TUPLE
# create a tuple of numbers
tupleNum = (3,6,8,1,7,5) 

# create program to print smallest number in tuple
def smallestNum(checkSmallNum):
    print("smallest number is",min(checkSmallNum))

# call function
smallestNum(tupleNum)

# 3: SET
# create a set of numbers
setA = {2,4,6,8,10}

# create a program to take each num from set and squared and return in setB
def newSet2(createSet2):
    return {i ** 2 for i in createSet2}

# call function in a variable
setB = newSet2(setA)
# print to check setB
print(setB)

# 4: DICTNARY
# create a dict of flavours
pizzaFlavours = {"one":"veg pizza", "two":"chicken tikka", "three":"Beef with extra cheese"}

# create a program to print keys from dict
def pizza(flavours):
    for i in flavours:
        print(i)
# call function with argument    
pizza(pizzaFlavours)