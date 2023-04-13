n = int(input())

positive_nums = []
negative_nums = []

for _ in range(n):
    integer = int(input())
    if integer >= 0:
        positive_nums.append(integer)
    else:
        negative_nums.append(integer)

print(positive_nums)
print(negative_nums)
print(f'Count of positives: {len(positive_nums)}')
print(f'Sum of negatives: {sum(negative_nums)}')
