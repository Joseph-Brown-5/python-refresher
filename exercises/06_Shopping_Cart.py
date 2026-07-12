# Shopping cart program

foods = []
prices = []
total = 0

# take user input
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

# print out your cart with prices and total value
print("Your Cart:")
n = 0
total = 0

for food in foods:
    print(f"{food}: ${prices[n]}")
    total += prices[n]
    n += 1

print(f"Your total is: ${total}")
