# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

def pizza ( diameter_in_cm, price):
    radius_m = (diameter_in_cm/2)/100
    area = radius_m * radius_m * 3.14
    return price/area

def main ():
    diameter_pizza1 = float(input("enter diameter of pizza 1"))
    price_pizza1 = float(input("enter price of pizza 1"))

    diameter_pizza2 = float(input("enter diameter of pizza 2"))
    price_pizza2 = float(input("enter price of pizza2"))

    price1 = pizza(diameter_pizza1, price_pizza1)
    price2 = pizza(diameter_pizza2, price_pizza2)

    print(f"Pizza 1 unit price: {price1:.2f} €/m²")
    print(f"Pizza 2 unit price: {price2:.2f} €/m²")

    if price1 < price2:
        print("Pizza 1 provides better value for money.")
    elif price2 < price1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value for money.")

main()
