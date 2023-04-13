def find_the_smallest_num(a, b , c):
    if a < b and a < c:
        return a
    elif b < a and b <c:
        return b
    elif c < a and c < b:
        return c


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(find_the_smallest_num(first_num, second_num, third_num))
