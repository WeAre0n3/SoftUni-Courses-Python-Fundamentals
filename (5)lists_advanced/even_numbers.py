nums = list(map(int, input().split(', ')))

found_indices = map(lambda x: x if nums[x] % 2 == 0 else 'no', range(len(nums)))

even_indices = list(filter(lambda a: a != 'no', found_indices))

print(even_indices)
