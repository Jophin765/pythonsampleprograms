"""
print("Welcome to Python Programing")
#getting user inputs
student_name=input("Enter your name: ")
student_age=int(input("Enter your age: "))
student_mark=float(input("Enter your mark: "))
is_present=bool(input("Is present or Not(T/F):"))
languages_known=input("Enter the languages known: ").split(",")
#printing the data
print("The Student name is : ",student_name)
print("The Student age is : ",student_age)
print("The student mark is: ",student_mark)
print("Present or not : ",is_present)
print("Languages known: ",languages_known)
#type fuction
print(type(student_name))
print(type(student_age))
print(type(student_mark))
print(type(is_present))
print(type(languages_known))
#id()-built in function that return unique identity of an object during its lifetime
num1=10
num2=10
num3=20
print(id(num1))
print(id(num2))
print(id(num3))

list1=[1,2,3]
list2=[1,2,3]
print(id(list1))
print(id(list2))"""

value1=25.6
value2=30
print(isinstance(value1,float))
print(isinstance(value2,float))
print(isinstance(value2,(int,float)))
#implicit type conversion
data1=10
data2=20.5
data3=data1+data2
print(data3)

data4="30"
data5="45" 
result=data4+data5
print(result)