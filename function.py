# declaring function
def sayHello():
    print("Hello World!")
    
# calling function
sayHello()

# function with return
def returnHello():
    return "Hello World!"

hello = returnHello()
print(hello)

# function with parameter/arguments
def sum(a, b):
    return a + b

result = sum(10, 15)
print(result)