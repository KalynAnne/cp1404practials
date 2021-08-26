import random

MAX = 45
MIN = 1
NUMBERS_PER_TICKET = 6


def main():
    number_of_picks = int(input("How many quick picks : "))
    while number_of_picks < 0:
        print("Try again!")
        number_of_picks = int(input("How many quick picks : "))
    for i in range(number_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_TICKET):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()

