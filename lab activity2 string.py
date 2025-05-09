#Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve”

input_str = "P@#yn26at^&i5ve"
chars = digits = symbols = 0
for ch in input_str:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")

#2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function”

input_str = "String and String Function"
result = ""
seen = set()
for ch in input_str:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("Output:", result)

# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”

input_str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper = lower = number = special = 0
for ch in input_str:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        number += 1
    elif not ch.isspace():
        special += 1
print("UpperCase :", upper)
print("LowerCase :", lower)
print("NumberCase :", number)
print("SpecialCase :", special)

#4. Write a Python Count vowels in a string
#input= “Welcome to Python Assignment”

input_str = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
count = sum(1 for ch in input_str if ch in vowels)
print("Total vowels are:", count)

