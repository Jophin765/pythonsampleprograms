""" 1.Arithmetic operator
2.Assignment 
3.Logical
4.Comparison
5.Bitwise
6.Membership
7.Identity"""
"""
print("arithmetic operator")
price_per_phone=20000
quantity=5
total_price=price_per_phone*quantity
average_price=total_price/quantity
gst_added=200
final_price=total_price+gst_added
discount_amount=1000
final_price=final_price-discount_amount
no_of_persons=3
remaining_price=final_price%no_of_persons
floor_divison=final_price//7
print(final_price)
print(floor_divison)
#assignement operator
score=100
score+=50
score-=20
score*=3
print(score)
#Logical
#and-both the conditions must be true
#or-any of the conditions must be true
#not-opposite of the condition
username="Jophin"
password="123"
entered_username=input("Enter the username : ")
entered_password=input("Enter the password: ")
if username==entered_username and password==entered_password:
    print("logged in Successfully")
else:
    print("Invalid")

day=input("Enter a day : ")
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working day")

logged_in=False
if not logged_in:
    print("Login Succesfull , Welcome User")
else:
    print("please login")
#Membership operator-checks whether the element is present or not
movies=["Batman","Spiderman","Man of Steel"]
movie=input("Enter a movie: ")
if movie in movies:
    print("Movie is Available")
else:
    print("Movie is Unavailable")
#not in
employees=["eve","sam","adam"]
employee=input("Enter the employee name: ")
if employee not in employees:
    print("Access denied")
else:
    print("Access granted")
#identity operator - checks whether memory location is same or not
value1=35
value2=35
print(value1 is value2)
print(value1==value2)

list1=[40,15,20,18]
list2=[40,15,20,18]
print(list1 is list2)
print(list1==list2)"""

a=5
b=3
print(a & b)
#0 1 0 1
#0 0 1 1
#0 0 0 1 - when and gate is used only 1 , 1 the result will be 1
print(a | b)
#0 1 0 1
#0 0 1 1
#0 1 1 1

print(a^b)

#0 1 0 1
#0 0 1 1
#0 1 1 0

print(~a)

print(5<<1)#5*1^2
print(5<<2)
print(5>>1)
print(5>>2)
