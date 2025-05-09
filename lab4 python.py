#1. Python program to check leap year.

     #code
def is_leap_year(year):
    # Leap year is divisible by 4
    # Except years divisible by 100, unless also divisible by 400
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Input from user
year = int(input("Enter a year: "))
# Check and print result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#2.Python Program to Find the Largest Among Three Numbers.

    #code
# Input three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
# Find the largest number
largest = max(num1, num2, num3)
# Print the result
print("The largest number is:",largest)

#3. Python Program to Check if a Number is Positive, Negative or 0.

     #code
# Input a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#4.Atoy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
#are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay
#after the discount.

     #code
# Input product code and order amount
product_code = int(input("Enter product code (1 for Battery, 2 for Key-based, 3 for Electrical): "))
order_amount = float(input("Enter order amount: "))
# Initialize discount and net amount
discount = 0.0
net_amount = order_amount
# Calculate discount based on product code and order amount
if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
        discount = order_amount * 0.10  # 10% discount
elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
        discount = order_amount * 0.05  # 5% discount
elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
        discount = order_amount * 0.10  # 10% discount
else:
    print("Invalid product code")
# Calculate net amount after discount
if product_code in [1, 2, 3]:
    net_amount = order_amount - discount
    print(f"Net amount to pay after discount: Rs. {net_amount:.2f}")


#5.A transport company charges the fare according to following table:
 #Distance
 #1-50
 #51-100
 #Charges
 #8 Rs./Km
 #10 Rs./Km
 #> 100
 #12 Rs/K

     #code
# Input distance traveled
distance = float(input("Enter the distance traveled (in km): "))

# Initialize fare
fare = 0.0

# Calculate fare based on distance
if distance > 0:
    if distance <= 50:
        fare = distance * 8  # 8 Rs./km for 1-50 km
    elif distance <= 100:
        fare = 50 * 8 + (distance - 50) * 10  # 8 Rs./km for first 50 km + 10 Rs./km for rest
    else:
        fare = 50 * 8 + 50 * 10 + (distance - 100) * 12  # 8 Rs./km for 50 km + 10 Rs./km for 50 km + 12 Rs./km for rest
    print(f"Total fare: Rs. {fare:.2f}")
else:
    print("Distance must be greater than 0")
