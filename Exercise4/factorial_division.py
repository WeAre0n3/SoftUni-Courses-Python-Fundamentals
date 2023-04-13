import math
from math import factorial


def calculate_factorial(a, b):
    first_factorial = math.factorial(a)
    second_factorial = math.factorial(b)
    result = first_factorial / second_factorial
    print(f'{result:.2f}')


first_int = int(input())
second_int = int(input())

calculate_factorial(first_int, second_int)
