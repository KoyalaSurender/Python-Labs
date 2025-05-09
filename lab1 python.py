#1 Write a program to print "Hello World"

print("Hello world!")


#2. Write a program to read int, float and string type values from console and print values.

#Read integer value
int_value=int(input("Enter an integer:"))
print("Integer value:",int_value)

#Read float value
float_value=float(input("Enter a float:"))
print("float value:",float_value)

#Read string value
string_value=(input("Enter an string:"))
print("string value:",string_value)


#3. Write a Python program to purposefully raise Indentation Error and correct it.
"""
#Program with Indentation Error
def check_number(num):
print("Checking number...")
if num > 0:
    print("Number is positive")
    elif num < 0:  # Indentation error: 'elif' is not aligned with 'if'
        print("Number is negative")
    else:
        print("Number is zero")
        # Test the function
check_number(5)
"""
#Corrected Program

def check_number(num):
    print("Checking number...")
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is zero")
# Test the function
check_number(5)
check_number(-3)
check_number(0)
