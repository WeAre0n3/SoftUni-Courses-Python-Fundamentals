import re

count = int(input())

for _ in range(count):
    barcode = input()

    pattern = r'^\@\#+[A-Z][A-Za-z0-9]{4,}[A-Z]\@\#+$'
    if re.match(pattern, barcode):
        if any(char.isdigit() for char in barcode):
            product_group = ''
            for s in barcode:
                if s.isdigit():
                    product_group += s
        else:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
