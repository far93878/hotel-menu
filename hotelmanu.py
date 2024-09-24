

Menu={
 'Pizza' : 200,
 'Next Cola ' : 100,
 'Burger '  :250
}
print("Welcome to FR 7 restaurant")
print("Pizza : Rs 200\nNext Cola : Rs 100\nBurger : Rs 250"     )
item_1 = input("Enter the name of item = ")
order_total =0
if item_1 in Menu:
    order_total += Menu[item_1]
    print(f"your item{item_1} hsa been added")
else:
    print(f"oder item{item_1} is not available")


other_oder = input(f" Do you want to oder some thing else ? (y/n )")
if other_oder =="y":
    item_2 = input("enter the name of item = ")
    if item_2 in Menu:
        order_total += Menu[item_2]
        print(f'order has been added')
    else:
        print(f"oder item{item_2} is not available")
print( f"Total amount = {order_total }")

