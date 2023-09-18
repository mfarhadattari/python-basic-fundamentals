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
