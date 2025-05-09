# 1. Write a python program to reverse a number using a while loop.

        
# Input a number
number = int(input("Enter a number: "))
# Store the original number for display
original_number = number
# Initialize the reversed number
reversed_number = 0
# Reverse the number using a while loop
while number > 0:
    digit = number % 10  # Extract the last digit
    reversed_number = reversed_number * 10 + digit  # Append digit to reversed number
    number = number // 10  # Remove the last digit from the original number
# Display the result
print(f"The reverse of {original_number} is: {reversed_number}")

#2. Write a python program to check whether a number is palindrome or not?

    
# Input a number
number = int(input("Enter a number: "))
# Store the original number
original_number = number
# Reverse the number using a while loop
reversed_number = 0
temp = number
while temp > 0:
    digit = temp % 10
    reversed_number = reversed_number * 10 + digit
    temp = temp // 10
# Check if the number is a palindrome
if original_number == reversed_number:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")

#3. Write a python program finding the factorial of a given number using a while loop.

    
# Input a number
number = int(input("Enter a number: "))

# Store the original number for display
original_number = number

# Initialize factorial and counter
factorial = 1

# Calculate factorial using a while loop
while number > 0:
    factorial *= number
    number -= 1

# Display the result
print(f"The factorial of {original_number} is: {factorial}")

#4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

        
# Initialize sum and variable to store input
total = 0
# Accept numbers until 0 is entered
while True:
    number = float(input("Enter a number (0 to stop): "))
    if number == 0:
        break  # Exit the loop if 0 is entered
    total += number  # Add the number to total
# Display the sum
print(f"The sum of all numbers is: {total}")
