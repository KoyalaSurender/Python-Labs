# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

       
# Declare the div() function
def div(a, b):
    result = a / b
    print(f"The division of {a} by {b} is: {result}")
# Call the function with two numbers
div(10,2)

#2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number.

# Declare the square() function
def square(num):
    result = num * num
    print(f"The square of {num} is: {result}")
# Call the function with a number
square(5)

#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

          
import random
# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]
# Display the numbers
print("The 5 random numbers are:", numbers)
# Find and display the maximum and minimum
print("Maximum number:", max(numbers))
print("Minimum number:",min(numbers))

#4. Accept a namefromthe user and display that in lower case using lower() function.

           
#Accept name from the user
name = input("Enter a name: ")
# Convert and display the name in lowercase
print("Name in lowercase:",name.lower())
