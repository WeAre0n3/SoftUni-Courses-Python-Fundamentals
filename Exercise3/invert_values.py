number_str = input().split()

inverted_str = []

for num in number_str:
    num = int(num)
    inverted_str.append(-num)

print(inverted_str)
