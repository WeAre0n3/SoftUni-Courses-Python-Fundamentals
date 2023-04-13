def sum_even_odd(a):
    sum_even = 0
    sum_odd = 0
    for ch in a:
        if int(ch) % 2 == 0:
            sum_even += int(ch)
        else:
            sum_odd += int(ch)
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


num = input()

sum_even_odd(num)
