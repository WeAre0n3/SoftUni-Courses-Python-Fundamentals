def is_num_perfect(a):
    divisors = []
    for num in range(1, a + 1):
        if a != num:
            if a % num == 0:
                divisors.append(num)
    if sum(divisors) == a:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

is_num_perfect(number)
