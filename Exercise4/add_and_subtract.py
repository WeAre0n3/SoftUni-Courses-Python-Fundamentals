def sum_one_two(a, b):
    return a + b


def subtract_three(c, d):
    return c - d


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = sum_one_two(first_num, second_num)

print(subtract_three(result, third_num))
