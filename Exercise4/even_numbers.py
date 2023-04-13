def check_if_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


nums_list = [int(x) for x in input().split()]

result_list = list(filter(check_if_even, nums_list))

print(result_list)
