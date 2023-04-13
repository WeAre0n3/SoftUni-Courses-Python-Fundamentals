n = int(input())

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for i in range(n):
    current_num = int(input())

    if current_num >= 0:
        positive_nums.append(current_num)
    else:
        negative_nums.append(current_num)

    if current_num % 2 == 0:
        even_nums.append(current_num)
    else:
        odd_nums.append(current_num)

command = input()

if command == 'positive':
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)
elif command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
