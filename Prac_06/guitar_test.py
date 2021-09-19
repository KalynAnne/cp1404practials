
from Prac_06.guitar import Guitar


def main():
    instrument1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    instrument2 = Guitar("Another Guitar", 2013, 5000)
    print(instrument1)
    print(instrument2)

    instruments = [instrument1, instrument2]
    for i in instruments:
        expected = input("what should be returned for age: ")
        print("{} get_age() - Expected {}. got {}".format(i.name, expected, i.get_age()))

    for i in instruments:
        expected = input("what should be returned for vintage status: ")
        print("{} is_vintage() - Expected {}. got {}".format(i.name, expected, i.is_vintage()))


main()
