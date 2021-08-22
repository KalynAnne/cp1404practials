"""Password checker"""

MIN_LENGTH = 6
password = input("Input Password: ")
while len(password) < MIN_LENGTH:
    print("INVALID LENGTH")
    password = input("Input Password: ")
for i in range(len(password)):
    print("*", end='')

