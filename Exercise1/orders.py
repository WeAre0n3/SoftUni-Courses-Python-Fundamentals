num_orders = int(input())

total_price = 0

for n in range(num_orders):
    price_per_cap = float(input())
    days = int(input())
    caps_per_day = int(input())
    if 0.01 <= price_per_cap <= 100 and 1 <= days <= 31 and 1 <= caps_per_day <= 2000:
        coffee_price = price_per_cap * days * caps_per_day
        total_price += coffee_price

        print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
