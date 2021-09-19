from Prac_06.guitar import Guitar

instruments = []


def main():
    print("My guitars!")
    name = "start"
    while len(name) != 0:
        name = str(input("Name: "))
        if len(name) != 0:
            year = int(input("Year: "))
            cost = int(input("Cost: "))
            instrument1 = Guitar(name, year, cost)
            instruments.append(instrument1)
        else:
            pass
    n = 0
    print("These are my guitars:")
    for i in instruments:
        n = n + 1
        print("Guitar {}: {} ".format(n, i,))


main()
