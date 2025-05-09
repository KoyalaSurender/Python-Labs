#1. Print the first 10 natural numbers using for loop

      
# Print first 10 natural numbers
for i in range(1, 11):
    print(i)

#2. Python program to check if the given string is a palindrome.

     
# Input a string
string = input("Enter a string: ")
# Remove spaces and convert to lowercase for accurate comparison
cleaned_string = string.replace(" ", "").lower()
# Reverse the string
reversed_string = cleaned_string[::-1]
# Check if the string is a palindrome
if cleaned_string == reversed_string:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")

#3. Python program to check if a given number is an Armstrong number.

      
# Input a number
number = int(input("Enter a number: "))
# Store the original number for display
original_number = number
# Calculate the number of digits
num_digits = len(str(number))
# Initialize sum of powers
sum_of_powers = 0
temp = number
# Calculate sum of each digit raised to the power of number of digits.

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10
# Check if the number is an Armstrong number
if original_number == sum_of_powers:
    print(f"{original_number} is an Armstrong number")
else:
    print(f"{original_number} is not an Armstrong number")

#4. Python program to get the Fibonacci series between 0 to 50.


    #code
    
# Initialize first two Fibonacci numbers
a,b=0,1

while b < 50:
    print(b)
    a,b=b,a+b

    

#5. Python program to check the validity of password input by user.

        
# Input password
password = input("Enter a password: ")

# Define password validation criteria
def is_valid_password(pwd):
    # Check length (must be at least 8 characters)
    if len(pwd) < 8:
        return False
    # Check for at least one uppercase letter
    if not any(c.isupper() for c in pwd):
        return False
    # Check for at least one lowercase letter
    if not any(c.islower() for c in pwd):
        return False
    # Check for at least one digit
    if not any(c.isdigit() for c in pwd):
        return False
    # Check for at least one special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in pwd):
        return False
    return True
# Check and display result
if is_valid_password(password):
    print("Password is valid!")
else:
    print("Password is invalid. It must contain:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (e.g., !@#$%^&*()_+-=[]{}|;:,.<>?")
