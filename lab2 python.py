#1. Calculate the multiplication and sum of two numbers

x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
sum=x+y
print("sum=",sum)
mul=x*y
print("mul=",mul)

#2.Declare two variables and print that which variable is largest using ternary operators

#Declare two variables and find the largest using if statement
var1 = float(input("Enter first variable: "))
var2 = float(input("Enter second variable: "))
if var1 > var2:
    largest = var1
else:
    largest = var2
print(f"The largest variable is: {largest}")

    
#3. Python program to convert the temperature in degree centigrade to Fahrenheit

#Program to convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

#4. Python program to find the area of a triangle whose sides are given
# Program to find the area of a triangle given its sides
import math

# Input the sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check if a triangle is valid (sum of any two sides > third side)
if a + b <= c or b + c <= a or a + c <= b:
    print("Invalid triangle: The sum of any two sides must be greater than the third side.")
else:
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    print(f"The area of the triangle is: {area:.2f} square units")
