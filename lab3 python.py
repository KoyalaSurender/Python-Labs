#1.using input()function take one number from the user and using ternary operators check whether the number is Even or Odd.

num=int(input("Enter a number:"))
print("Even"if num%2==0 else "odd")#ternary operators

#2.Using input function take two number and then swap the number.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Swapping the numbers
a, b = b, a

print("After swapping:")
print("First number:",a)
print("Second number:",b)


#3.Write a program to convert kilometersto miles.

# Get input from the user
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor
conversion_factor = 0.621371
# Calculate miles
miles = kilometers * conversion_factor
# Display result
print(f"{kilometers} kilometers is equal to {miles}miles")

#4.Find the simple interest on RS.200 for 5 years at 5% per year.

# Define the values
principal = 200  # Amount in Rs.
rate = 5         # Rate of interest in percentage
time = 5         # Time in years
# Calculate simple interest
simple_interest = (principal * rate * time) / 100
# Print the result
print(f"Simple Interest = Rs. {simple_interest}")
