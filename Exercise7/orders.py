command = input()

product_list = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in product_list:
        product_list[name] = {"price": price, "quantity": quantity}
    else:
        product_list[name]["price"] = price
        product_list[name]["quantity"] += quantity
    command = input()

for product, price_quantity in product_list.items():
    total = price_quantity["price"] * price_quantity["quantity"]
    print(f"{product} -> {total:.2f}")
