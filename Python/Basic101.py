"""varibles in python"""
#Variables in Python are names that store data.
# a="Rohan Reddy"
# age = 20
# print(f"My Name is {a} and my Age is {age}")
'''Data-Types'''
""" Primitive immutable data types in Python are:
These can’t be changed in place; any “change” makes a new object."""

# int – integers

# float – decimal numbers

# bool – True / False

# str – text

# NoneType – None

# x = 5
# print(id(x))   # memory id of 5
# x = x  +1    # creates a NEW int object 6
# print(id(x))   # different id
'''Operators'''

"""️⃣ Arithmetic"""

#+ - * / % // **
# print(10+1)
# print(10-2)
# print(10/2)
# print(10//2)
# print(2**2)
"""⃣ Comparison (Relational)"""
# print(10!=10)
# print(10 <= 8)
# print(10 >=5)

""""️⃣ Assignment"""
#= += -= *= /= //= %= **=
# a=10;
# a+=10;// a=10+10
# print(a)


""" Logical"""

#and or not
# print(True or False)


""" Membership"""

#in not in

# a=[1,2,3]
# print(20 in a)

""" Identity"""

#is is not


'''Type Casting'''


"""Type casting means converting a value from one data type to another in Python.
Two kinds: implicit (done automatically) and explicit (you do it).
    """

#1. Implicit Casting
num1=10
num2=5.3
num3=num1+num2
print(num3)


#Explicit Casting
# n="10"
# b=int(n)
# print(type(b))


'''user input'''
# A=int(input("Enter Number A"))
# B=int(input("Enter Number B"))
# C=A+B;
# print(C)
"""You can take user input in Python using the built-in input() function"""

'''Strings'''
"""Strings in Python are immutable sequences of characters used to store text."""

#Accessing
# text = "Python"
# print(text[0])
# print(text[-4:-2])
# print(text[1:4])



# Common Methods
msg = "  Hello World  "
print(msg.lower())
print(msg.upper())
print(msg.strip())
print(msg.replace("World","Python"))
print(msg.split())


# Concatenation & Repetition
# a = "Hi"
# # b = "There"
# # print(a + " " + b) 
# # print(a * 3)


# ''''LIST'''
# nums = [10, 20, 30, 40, 50];
# # data=[20,2.3,"rohan",True]
# # print(data)
# print(nums[0])
# print(nums[-2])
# print(nums[1:4]) 

# # Original list
# nums = [5, 2, 7]
# print("Original:", nums)

# # append(x) - add to end
# nums.append(10)
# print("append(10):", nums)

# #  extend(iterable) - add multiple items
# nums.extend([1, 3])
# print("extend([1,3]):", nums)

# # insert(i, x) - insert at index
# nums.insert(2, 99)
# print("insert(2,99):", nums)

# # remove(x) - remove first matching value
# nums.remove(99)
# print("remove(99):", nums)

# # pop([i]) - remove & return last (or index)
# popped = nums.pop()
# print("pop():", popped, nums)

# #  clear() - remove all items
# nums_copy = nums.copy()  # keep a copy for later
# nums.clear()
# print("clear():", nums)

# # Restore list for further examples
# nums = nums_copy

# #  count(x) - count occurrences
# nums.append(7)
# print("count(7):", nums.count(7))

# #  sort() - sort in place
# nums.sort()
# print("sort():", nums)

# # reverse() - reverse list
# nums.reverse()
# print("reverse():", nums)

# #copy() - shallow copy
# copy_list = nums.copy()
# print("copy():", copy_list)

# '''Tuple'''
# t1 = (1, 2, 3)
# t2 = ("a", "b", "c")
# t3 = (1, "a", 3.5)

# nums = (10, 20, 30, 40, 50)
# print(nums[0])
# print(nums[-1])
# print(nums[1:4])


# ''''Dictionary (dict)'''

# """A dictionary is an unordered collection of key-value pairs. Keys are unique, values can be anything."""

# # Empty dictionary
# # d1 = {}

# # With key-value pairs
# d2 = {"a": 1, "b": 2, "c": 3}

# print(d2["a"])       
# print(d2.get("b"))  
# print(d2)


# # d2["d"] = 4          # add new key-value
# # d2["a"] = 10         # update existing


# # print(d2.keys()) 

# # print(d2.items()) 



# '''Set'''

# """A set is an unordered collection of unique elements. no duplicates"""

# s1 = {1, 2, 3, 4}
# s2 = set([1, 2, 2, 3])  # duplicates removed → {1,2,3}


# s1.add(5)       # {1,2,3,4,5}
# s1.remove(2)    # {1,3,4,5}, error if 2 not present
# s1.pop()        # removes random element
# s1.clear()      # removes all

# print(s1)


'''Conduction Statements'''

""""statements that allow your program to make decisions based on conditions."""

#if statement


x = 10
if (x > 5):
    print("x is greater than 5")

# #if-else statement


x = 3
if (x > 5):
    print("x > 5")
else:
    print("x <= 5")

# #if-elif-else statement

x = 7
if (x > 10):
    print("x > 10")
elif( x > 5):
    print("x is between 6 and 10")
else:
    print("x <= 5")



'''Loops'''
#for loop


# Print numbers 1 to 5
# for i in range(1, 6):
#     print(i)


#while loop

# Print numbers 1 to 5
# i = 1
# while (i < 5):
#     print(i)
#     i += 1


# break
# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)   


# continue
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)


"""Functons"""

"""A function is a block of reusable code that performs a specific task. Functions help organize code, reduce repetition, and improve readability."""


#Defining a Function

def greet():
    print("Hello, World!")

greet()  # Call the function


# #Function with Parameters

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")


# #Function with Return Value

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# #Default Parameters

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest!
greet("Alice")  # Hello, Alice!
