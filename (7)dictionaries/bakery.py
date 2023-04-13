stock = input().split()

bakery = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    value = int(stock[i + 1])
    bakery[key] = value

print(bakery)
