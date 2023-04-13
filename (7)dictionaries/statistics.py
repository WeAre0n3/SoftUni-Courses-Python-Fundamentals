command = input()
products = {}

while command != 'statistics':
    command_list = command.split(': ')
    product = command_list[0]
    quantity = int(command_list[1])
    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity
    command = input()

print('Products in stock:')
for (product, quantity) in products.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')
