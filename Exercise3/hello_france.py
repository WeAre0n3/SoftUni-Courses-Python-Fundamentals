items = input().split("|")
init_budget = int(input())

budget = init_budget
profit = 0
total = 0
reached = False

for item in items:
    current = item.split("->")
    value = float(current[1])

    if value > budget:
        continue
    elif current[0] == "Clothes" and value > 50:
        continue
    elif current[0] == "Shoes" and value > 35:
        continue
    elif current[0] == "Accessories" and value > 20.50:
        continue

    budget -= value
    new_value = value * 1.4
    profit += new_value - value
    total += new_value
    print(f"{new_value:.2f}", end=" ")
    if total + budget >= 150:
        reached = True

print()
print(f"Profit: {profit:.2f}")

if reached:
    print("Hello, France!")
else:
    print("Not enough money.")
