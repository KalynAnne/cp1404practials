"""Password checker"""

MIN_LENGTH = 6


def main():
    password = get_password()
    while len(password) < MIN_LENGTH:
        print("INVALID LENGTH")
        password = get_password()
    get_asterisks(password)


def get_password():
    return input("Input Password: ")


def get_asterisks(password):
    for i in range(len(password)):
        print("*", end='')


main()
