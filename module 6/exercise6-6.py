def price_calculator_of_pizza(diameter, price):
    radius = (diameter / 100) / 2
    return price/(radius*radius*3.14)


d1 = float(input("Enter diameter of first pizza (in cm): "))
p1 = float(input("Enter Price of first pizza (in euro): "))

d2 = float(input("Enter diameter of second pizza (in cm): "))
p2 = float(input("Enter Price of second pizza (in euro): "))

pizza1_price = price_calculator_of_pizza(d1, p1)
pizza2_price = price_calculator_of_pizza(d2, p2)

if pizza1_price > pizza2_price:
    print(f"pizza 2 ({pizza2_price:.2f} euro/m2) is cheaper than pizza 1 ({pizza1_price:.2f} euro/m2) ")
elif pizza1_price==pizza2_price:
    print(f"pizza 1 ({pizza1_price:.2f} euro/m2) and pizza 2 ({pizza2_price:.2f} euro/m2 has the same amount \n so, it is equal in price ")
else:
    print(f"pizza 1 ({pizza1_price:.2f} euro/m2) is cheaper than pizza 2 ({pizza2_price:.2f} euro/m2) ")