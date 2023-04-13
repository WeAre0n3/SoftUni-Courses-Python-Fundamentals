stock = input().split()
bakery = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    bakery[key] = int(value)

searched_products = input().split()

for product in searched_products:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
