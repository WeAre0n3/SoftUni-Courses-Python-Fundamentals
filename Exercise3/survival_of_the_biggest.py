integers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    number_to_remove = min(integers)
    integers.remove(number_to_remove)

print(', '.join([str(x) for x in integers]))
