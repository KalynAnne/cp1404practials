"""Displays all odd numbers between 1 and 20 with a space between each one"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a.count in 10s from 0 to 100"""
for i in range(0, 110, 10):
    print(i, end=' ')
print()

"""b.count down from 20 to 1"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""print n starts"""
stars = int(input("How many starts shall I print? "))
for i in range(stars):
    print("*", end='')

"""print n lines of increasing stars"""
stars = int(input("How many starts shall I print? "))
for stars in range(0, stars):
    for i in range(0, stars + 1):
        print("*", end='')
    print()

