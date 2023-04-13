import re

input_count = int(input())

for _ in range(input_count):
    string = input()
    pattern = r'^!([A-Z][a-z]{3,})!\:\[([A-Za-z]{8,})\]$'
    if re.match(pattern, string):
        string_list = re.findall(pattern, string)
        nums = []
        for l in string_list[0][1]:
            nums.append(ord(l))

        print(f'{string_list[0][0]}: {(" ".join(map(str, nums)))}')
    else:
        print('The message is invalid')
