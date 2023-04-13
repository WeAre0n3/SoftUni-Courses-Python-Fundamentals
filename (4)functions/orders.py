def total_price(product, quantity):
    if product == 'coffee':
        return 1.50 * quantity
    elif product == 'coke':
        return 1.40 * quantity
    elif product == 'water':
        return 1.00 * quantity
    elif product == 'snacks':
        return 2.00 * quantity


product_name = input()
current_quantity = int(input())

print(f'{total_price(product_name, current_quantity):.2f}')
