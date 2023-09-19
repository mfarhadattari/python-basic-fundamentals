# PYTHON BASIC FUNDAMENTAL

## Topics

- Introduction and Output
- Variable and Data type
- Input
- Operators
- Condition
- List
- Loop
- Function

## Output

In python there is a built-in function for display output. That is print() function.

```python
print("Hello World!")
```

## Comments

- Single line Comments: # Comment
- Multiline Comments: """ Comments """

```python
# This is Single line comment

"""
This is
Multiline Comment
"""
```

## Variable

Variable is the container of storing value in memory. It is the name of memory location where data will store.

```python
variable_name = value
```

```python
name = "Mohammad Farhad"
age = 19
print(name, age)
```

## Data Types

- string : text or character which inside on single quotes or double quotes.
- number : integer or float number
- boolean: True or False value

```python
name = "Mohammad Farhad"
age = 19
temperature = 100.5
isMarried = False
```

## Input

In python their is a built in function which take input from user that is input().

```python
input(placeholder string)
```

```python
name = input("What is your name: ")
print("Hello! ", name)
```

### Input function take input string. So that we need to casting it on our expected datatype

```python
int()
float()
bool()
```

```python
name = input("What is your name: ")
age = int(input("Enter your age: "))
gpa = float(input("What is your gpa: "))
isMarried = bool(input("Are you married: "))
print("Hello! ", name, "Age: ", age, "GPA: ", gpa, "isMarried: ", isMarried)
```

## Operator

Operator is used to perform operation in data.

- Arithmetic Operator (+, -, \*, /, //, %)
- Relational Operator (> , <, >=, <=, ==, !=)
- Logical Operator (and , or, not)
- Assignment Operator (=, +=, -=, \*=, /=)

### Arithmetic Operator-

```python
a = int(input("A = "))
b = int(input("B = "))

sum = a + b
deference = a - b
multiplication = a * b
division = a / b
floorDivision = a // b
reminder = a % b

print("Sum= ", sum)
print("Deference= ", deference)
print("Multiplication= ", multiplication)
print("Division= ", division)
print("Floor Division= ", floorDivision)
print("Reminder= ", reminder)
```

### Relational Operator

```python
num1 = 23
num2 = 40
print(num1 > num2) # False
print(num1 < num2) # True
print(num1 >= num2) # False
print(num1 <= num2) # True
print(num1 == num2) # False
print(num1 != num2) # True
```

### Logical Operator

```python
admittedClass = 4
gpa = 5.00

print(admittedClass == 5 and gpa >= 4.40) # return true if all true
print(admittedClass == 5 or gpa >= 4.40) # return true if one true
print(not admittedClass == 5) # return true if opposite
```

### Assignment Operator

```python
num1 = 38
print(num1)
num1 += 5
print(num1)
num1 -= 10
print(num1)
num1 *= 5
print(num1)
num1 /= 2
print(num1)
```

## Condition

- if else
- elif

```python
age = int(input("Age = "))
if(age >= 18 and age<= 35):
    print("You are a young!")
elif(age >= 36):
    print("You are older!")
else:
    print("You are a child!")
```

## List

List is a collection of data separated by comma inside square bucket. List index start from 0.

```python
list_name = [data]
```

```python
numbers = [1, 2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]

# access by index
print(numbers[2]) # 3

# get index num
print(numbers.index(5)) # 4

# change value
numbers[1] = 0
print(numbers) # [1, 0, 3, 4, 5]

# length
print(len(numbers)) # 5

# add item in last
numbers.append(6)
print(numbers) # [1, 0, 3, 4, 5, 6]

# remove a item
numbers.remove(0)
print(numbers) # [1, 3, 4, 5, 6]

# min number of list
print(min(numbers)) # 1

# max number of list
print(max(numbers)) # 6

# item exist in list
print(3 in numbers) # True

# not exist in list
print(9 not in numbers) # True

# concat list
print(numbers + [8,9]) # [1, 3, 4, 5, 6, 8, 9]

# remove last item
numbers.pop()
print(numbers) # [1, 3, 4, 5]

# add item using index
numbers.insert(1, 2) # [1, 2, 3, 4, 5]
print(numbers)

# sort list
numbers2 = [1, 5, 0, 9, 5]
numbers2.sort()
print(numbers2) # [0, 1, 5, 5, 9]
numbers2.sort(reverse= True)
print(numbers2) # [9, 5, 5, 1, 0]

# reverse list
numbers2.reverse()
print(numbers2) # [0, 1, 5, 5, 9]

```
