"""
#lambda function
new_list=[1,2,7,8,5]
squared_list=list(map(lambda item:item*item,new_list))  # noqa: C417
print(squared_list)
odd_list=list(filter(lambda item:item%2!=0,new_list))  # noqa: C417, RUF100
print(odd_list)



# Create a list of tuple and sort age wise
list_of_tuples = [("John", 25, "TVM"), ("C.C", 30, "Kochi"), ("Rize", 20, "Kottayam")]
sorted_list = sorted(list_of_tuples, key=lambda item: item[1])
print(sorted_list)



employee_dict={"John":25,"C.C":30,"Rize":20}
sorted_employee_dict=sorted(employee_dict.items(),key=lambda item:item[1])
print(sorted_employee_dict)


# Reduce function
from functools import reduce

elements = [1, 2, 3, 4, 5]
sum_of_elements = reduce(lambda x, y: x + y, elements)
print(sum_of_elements)  # eg 1+2=3 3+3=6 6+4=10 10+5=15


# pure function - same input that will provide same output
def addition(num1, num2):
    return num1 + num2
print(addition(2, 3))  # eg 2+3=5
print(addition(2, 3))  


def pure_function(numbers):# second characteristic of pure function is that it does not have any side effects(input values will not change but output will)
    new_list=[]
    for items in numbers:
        new_list.append(items*2)
    return new_list
#print(pure_function([1,2,3,4,5]))    # eg 1*2=2 2*2=4 3*2=6 4*2=8 5*2=10
original_list=[1,2,3,4,5]
modified_list=pure_function(original_list)
print(modified_list)
print(original_list)  # original list will not change


#First class function 
#assign a function to a variable

def greet(name):
    return f"Hello, {name}"
print(greet("John"))

message=greet("John")
print(message)

#passing function as an argument
def greet():
    print("Hello")
def display(func):
    func()
display(greet)


#returning function from another function
def outer():
    def inner():
        print("Hello from inner function")
    return inner
result=outer()
result()
"""

#store function in a list
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
functions=[add,subtract]
print(functions[0](5, 3))  # Output: 8

#Higher order function

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def calculate(operation, x, y):
    return operation(x,y)
print(calculate(add, 5, 3))  # Output: 8
