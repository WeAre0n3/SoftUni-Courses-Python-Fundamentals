from math import ceil
num_sequence = [int(x) for x in input().split(', ')]

low_boundary = 1
high_boundary = 10

groups_count = ceil((max(num_sequence) / 10))

for i in range(1, groups_count + 1):
    grouped_numbers = [x for x in num_sequence if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * i}'s: {grouped_numbers}")

    low_boundary += 10
    high_boundary += 10
