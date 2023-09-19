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

### Input function take input string. So that we need to convert it on our expected datatype

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
