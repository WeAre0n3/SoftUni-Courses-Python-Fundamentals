str_list = input().split(', ')

for el in str_list:
    if el == '0':
        str_list.append(str_list.pop(str_list.index(el)))

int_list = [eval(i) for i in str_list]

print(int_list)
