Dynamic Type System
Readability
Interpreted
Multi-Paradigm :*OOPS, Structure Oriented and Embraces functional Programming as well*

Python Enhancment Proposal Process => PEP


Areas Python is used
- Linux Scripting & Admin
- Web Development
- App Scripting
- Data Science (*BigData, ML*)

	

Python 
- Executing python file
- Rudimentary REPL
PIP
- PIP installs packages
- uninstall packages
- package groups
- dependancies
- make sure right versions are used. 
- `pip install <packagename>`
ipython
- List itemrobust interactive shell
	
python.org
docs.python.org

PEP - Python Enhancement Proposal

pypi - python package index

pypi.pyathon.org

**Python 2** 

- pip
- python
- ipython
- Legacy
- used if no control over environment.
- Libraries that are not compatible with python 3


**Python 3**
- Intentionally not backward compatible
- pip3
- python3
- ipython3


Executing Python Code
 - Interpretor 
- REPL
- Natively



Python is dynamically typed. Type is infered.



**Setup**
VS Code : Install Python Extension
MyPy linter

Set default interpreter to Python3.x

Check lintOnSave (File→ Preferences)
Code-runner-Executor Map update for user and set Python3 instead of Python -u
Ctrl + Alt + N to run (Code Runner is REad-Only)

Base Types are not mutable. Each new value creates new address.
List is Mutable

**Basic String Stuff**
Concatenation
```
first = "Jayaraj"
last = "Sivadasan"
full = f"{first} {last}"

print(full)

course = " Hello WOrld "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip().lower())
print(course.rstrip())
print(course.find("WO"))
print(course.replace("W", "*"))
print("Hello" in course)  # IsExisting
```

**Numbers**
```
x = 10
print(bin(x))  # print in binary
print(hex(x))  # print in hexadecimal
```
# Complex Numbers: a + bi  -- in python j is imaginary number.
```
x = 1+2j
print(x)


x = 10+3
print(x)
x = 10-3
print(x)
x = 10*3
print(x)
x = 10/3
print(x)
x = 10//3
print(x)
x = 10 % 3
print(x)
x = 10 ** 3  # 10^3
print(x)

x += 1  # x= x+1 . Augmented Assignment. No increment/ decryment operators
print(x)
```
https://docs.python.org/3/library/functions.html
For Mathematical functions import math moudle. 
**Boolean**
```
print(bool(""))  # False
print(bool(" "))  # True
print(bool(0))  # False
print(bool(1))  # True
print(bool(-12))  # True
print(bool([]))  # False
print(bool([3, 4]))  # True
```

# logical operators
```
name = "Jayaraj"
```
# NOT
```
if not name.strip():
    print("Empty")
else:
    print("Not Empty")
# NOT
age = 22
if age >= 18 and age < 65:
    print("Eligible")
else:
    print("Not eligible")
```
# Chaining comparison operators. The above if-else becomes

```
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not Eligible")

```
# Ternary Operator (? in C#)
```
message = "Eligible" if age >= 18 else "Not Eligble"
print(message)


for x in "PYthon":
    print(x)

for x in ['A', 'B', 'C']:
    print(x)

for x in range(5):
    print(x)
```

**While Looop**
```
guess = 0
answer = 5


while answer != guess:
    guess = int(input("Guess: "))
```

**Dictionary**
```
def save_user(**user):
    print(user)


save_user(id=1, name="admin")
```
Output: 

`{'id': 1, 'name': 'admin'}`


**Scope**
There is no block level scope like Java & C#
A variable defined in a function is accessible across the function.

If a variable is kept outside of all functions it becomes a global variable. Accessible by all functions in that file.


**Example**
```
# FizzBizz problem
# divisible by 3 Fizz divisible by 5 Buzz divisible by both FizzBuzz
# Else return input

def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return 'Fizz Buzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input


print(fizz_buzz(5))  # Expected Output: Buzz
print(fizz_buzz(3))  # Expected Output: Fizz
print(fizz_buzz(15))  # Expected Output: FizzBuzz
print(fizz_buzz(7))  # Expected Output: 7

```


## List
```
#Every object in a list can be of a different type.
letters = ["a", "b", "c"]  # Initialize a list
matrix = [[0, 1], [0, 2], [0, 3]]
zeroes = [0]*5  # list with 5 zeroes.
combined = zeroes + letters  # combine two lists with + operator
print(combined)
numbers = list(range(30))  # create alist of numbers using range function
print(numbers)
chars = list("Hello World")  # create a list from a string.
print(chars)

print(len(chars))  # len function
```
```
letters = ["a", "b", "c"]  # Initialize a list
print(letters)  # prints entire list

print(letters[0])  # prints a
print(letters[-1])  # prints last itme c


letters[0] = "A"  # Modify the first item
print(letters)  # prints entire list


print(letters[0:3])  # new list with fist 3 items
print(letters[:3])  # new list with fist 3 items
print(letters[0:])  # all items
print(letters[:])  # allitems copy
print(letters[::2])  # every second item

numbers = list(range(20))
print(numbers[::2])  # print all even numbers up to 20

print(numbers[::-1])  # reverse order

#List unpacking. Count should be equal

numbers = [1,2,3]
first, second, third = numbers. 

```

### Enumerating and Unpacking a list
```
# Enumerate a list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in enumerate(letters):
    print(letter)   # returns a tuple. Index and item at index.

# Unpack the touble in the loop itself

for index, letter in enumerate(letters):
    print(index, letter)
```

### Adding & Removing items from a list.
```

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# adding an item to the list

letters.append('A')
print(letters)

letters.insert(27, 'B')
print(letters)


# remove an item from the list

letters.pop(27)
print(letters)

# remove an item using del method

del letters[26]
print(letters)


# remove an item for which index is not known
letters.remove('x')  # Removes the first occurrance of x
print(letters)
```

### Finding an item in a list

```
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# find an item's Index
print(letters.index('b'))

# find an item that does not exist
if('B' in letters):
    print(letters.index('B'))
```

#### Sorting

```
letters.sort(reverse=True)

print(letters)

print(sorted(letters))  # returns a sorted list. DOes not modify original list
print(letters)

```

### Sorting List of Touples

```
items = [
    ("Product1", 10),
    ("Product2", 90),
    ("Product3", 21),
    ("Product4", 30),
    ("Product5", 56),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

```
## LAMBDA
### Better way to write the above using Lambda
```
items = [
    ("Product1", 10),
    ("Product2", 90),
    ("Product3", 21),
    ("Product4", 30),
    ("Product5", 56),
]


items.sort(key=lambda item: item[1])
print(items)
```

### Mapping
```
items = [
    ("Product1", 10),
    ("Product2", 90),
    ("Product3", 21),
    ("Product4", 30),
    ("Product5", 56),
]

# Create an iterable that contains only prices from the above list
# Lambda is invoked for everyitem and the 1th position of the touple is returned and added to a Map object
# convert the map object to a list as any iterable can be converted in to a list.
x = list(map(lambda item: item[1], items))
print(x)

```

#### Map in a different way
```
# [expression for item in items]
prices = [item[1] for item in items]
print(prices)
```

### Filtering

```
## takes filter expression as a lambda and returns a Filter object which is iterable
## convert the filter object in to a list.
x = list(filter(lambda item: item[1] >= 10, items))
print(x)
```

#### Filter in a different way

```
# Filter in a different way
# [expression for item in items]
filtered = [item for item in items if item[1] > 10]
print(filtered)
```

### Zip

zip(*iterables) --> A zip object yielding tuples until an input is exhausted.

       list(zip('abcdefg', range(3), range(4)))  
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]  
The zip object yields n-length tuples, where n is the number of iterables passed as positional arguments to zip(). The i-th element in every tuple comes from the i-th iterable argument to zip(). This continues until the shortest argument is exhausted.


### Generator
```
from sys import getsizeof
# Generators
# does not store values in memory
# the size of the generator object does not change

values = (x*2 for x in range(100000000))
print("gen:", getsizeof(values))
# print(values)
# for x in values:
#     print(x)


## Generator does not support len
```

### Unpacking Operator

```
	numbers = [1,2,3]
	print(*numbers)
	
otuput: 
	1 2 3
	

Examples:
	values = [*range(5)] # unpack a list
	valeus = *"Hello World" # unpack a string
	
	#Unpacking dictionaries
first = {"x": 1}
second = {"x": 10, "y": 2}

combined = {**first, **second, "z": 1}
print(combined)

	
	
```

### Module In Python

a module is a file with code that handles similar stuff.
Example:
```
sales.py

def calculate_tax():
    print('calculating tax...')


def calculate_shipping():
    print('calculating shipping...')


```
You can import in the following ways:

```
app.py

from sales import calculate_shipping, calculate_tax
import sales
sales.calculate_tax()

```



#This is how we write CSV file in python:

```
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1, 1000, 90.65])
    writer.writerow([2, 1001, 40.75])
    writer.writerow([3, 1001, 40.75])
```

Note that if the file is named csv.py , then when you import csv you will get erro. 
