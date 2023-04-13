def is_palindrome(current_list):
    for num in current_list:
        if num == num[::-1]:
            print('True')
        else:
            print('False')


list_num = input().split(', ')

is_palindrome(list_num)
