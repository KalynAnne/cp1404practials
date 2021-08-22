"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
print("Calculate sales until negative value is entered")
sales = float(input("Enter sales: $"))
while sales >= 0:
    if 1000 > sales >= 0:
        bonus_percentage = 0.1
        bonus_calculated = sales * bonus_percentage
        print("Your bonus is $", bonus_calculated)
    elif sales > 999:
        bonus_percentage = 0.15
        bonus_calculated = sales * bonus_percentage
        print("Your bonus is $", bonus_calculated)
    else:
        print("Invalid option")
    sales = float(input("Enter sales: $"))
print("Thanks for calculating your bonus.")

