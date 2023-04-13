def result(grade):
    if 2.00 <= grade <= 2.99:
        return 'Fail'
    elif grade <= 3.49:
        return 'Poor'
    elif grade <= 4.49:
        return 'Good'
    elif grade <= 5.49:
        return 'Very Good'
    elif grade <= 6.00:
        return 'Excellent'


grade_data = float(input())

print(result(grade_data))
