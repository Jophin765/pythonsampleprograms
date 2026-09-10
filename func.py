"""
def funtion_name(parameters):
    code to be executed

def welcome():
    print("Welcome Jophin")
welcome()

def greeting(username,userage):
    print(f"Welcome {username},you are {userage} years old")
greeting("Jophin",22)

def addition(num1,num2):
    return num1+num2
num1=int(input("Enter the first No: "))
num2=int(input("Enter the Second No: "))
print(addition(num1,num2))

#Positional Arguments
def book_ticket(moviename,customername,seats,ticketprice):
    totalprice=seats*ticketprice
    return f"{customername} booked {seats} tickets for {moviename}. Total amount is :{totalprice}"
print (book_ticket("Batman","Jophin",5,250))

#Keyword Argument
def customer_details(customername,customerage,city):
    print(f"{customername} is {customerage} yrs old and lives in {city}")
customer_details(customerage=22,customername="Jophin",city="Trivandrum")

#default arguments
def booking_status(customername="Jophin",status="Confirmed",screen="Screen 1"):
    print(f"{customername} booking status is {status} and the screen allocated is {screen}")
booking_status()
booking_status("Eve")
booking_status("Tom","Pending")
booking_status("Jerry","Pending","Screen 3")

#Muliple Arguments

def calculate_bill(*ticketprices):
    print(f"ticketprices : {ticketprices}")
calculate_bill(150,101,115,128,100)

#Built in Function

print(len("Jophin"))
print(sum([1,2,3,4,5]))
print(min([2,4,5,6,7]))
print(max([7,8,5,6,9]))
print(sorted([22,88,9,4,56]))
print(sorted([22,88,9,4,56],reverse=True)) #For Descending order

#legb rule

def student_details():
    name="Jophin"
    print("student name: ", name)
student_details()
print("student name: ", name)

#global variable

college_name="mar ivanios college"
def display():
    print("college name: ",college_name)
display()
print("college name: ",college_name)

#enclosing variable

def department():
    department_name="Cs"
    def student():
        print("department name",department_name)
    student()
department()


tax=50#global variable
def shopping():
    discount=100# enclosing variable
    def bill():
        amount=2500
        total_amount=amount-discount+tax
        print("Total amount is: ",total_amount)
    bill()
shopping()

#RECURSIVE FUNCTION 
def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
num=int(input("Enter a Number "))
print(factorial(num))


#working - 
6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(3)
6*5*4*3*factorial(2)
6*5*4*3*2*factorial(1)   

#lamba function
#lambda arguments:expression   synatax

def add(num1,num2):
    return num1+num2
print(add(3,6))


add=lambda a,b:a+b
print(add(7,8))

square=lambda num:num*num
print(square(7))

celsius_to_f =lambda c:(c*9/5)+32
print(celsius_to_f(100))

multiply=lambda a,b:a*b
print(multiply(7,8))

cube=lambda x:x**3
print(cube(3))

is_odd=lambda x:x%2!=0
print(is_odd(7))

smallest=lambda a,b,c:min(a,b,c)
print(smallest(8,7,2))

area=lambda l,b:l*b
print(area(110,128))"""


