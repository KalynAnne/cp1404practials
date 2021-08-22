
total = 0
number_of_items = int(input("Number of items: "))
# check whether the input is greater than or equal to zero for validity
while number_of_items < 0:
    print("invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total = total + price_of_item
# apply a discount if total > 100. Discount is 10%
if total > 100:
    discounted_total = total * 0.1
    total = total - discounted_total
print("Total: ${:.2f} ".format(total))



