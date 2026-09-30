"""
print("Hello Python")

#Addition

num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")


#Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:

    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
print(f"Division: {num3} / {num4} = {div_result}")

#Area of Triangle

base = float(input("Enter the length of the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
# Calculate the area of the triangle
area = 0.5 * base * height
# Display the result
print(f"The area of the triangle is: {area}")

# Swapping
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Swapped values: a = {a}, b = {b}")

#Generate a random no
import random

print(f"Random number: {random.randint(1, 100)}")


# Km Conversion
kilometers = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
"""
# Calendar

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)
