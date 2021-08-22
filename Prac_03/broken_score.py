"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random
# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    while score >= 0:
        print(determine_result(score))
        score = float(input("Enter score: "))
    score = random.randint(0, 100)
    print("The score", score, "is", determine_result(score))


def determine_result(score):
    if score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    elif score < 50:
        result = "Bad"
    else:
        result = 'Invalid score'
    return result


main()
