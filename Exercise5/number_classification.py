nums_list = [int(x) for x in input().split(', ')]

positive_nums = [str(x) for x in nums_list if x >= 0]
negative_nums = [str(x) for x in nums_list if x < 0]
even_nums = [str(x) for x in nums_list if x % 2 == 0]
odd_nums = [str(x) for x in nums_list if x % 2 != 0]

print(f'Positive: {", ".join(positive_nums)}')
print(f'Negative: {", ".join(negative_nums)}')
print(f'Even: {", ".join(even_nums)}')
print(f'Odd: {", ".join(odd_nums)}')
