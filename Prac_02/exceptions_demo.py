"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# A Value error will occur when numerator is negative number

2. When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur when denominator is set to 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# You could make entering a 0 an end to a loop
# You could have the console print NA as the value

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


