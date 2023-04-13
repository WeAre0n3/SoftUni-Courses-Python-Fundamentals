strings = input().split()

str1 = strings[0]
str2 = strings[1]
min_len = min(len(str1), len(str2))

str_sum = 0

for idx in range(min_len):
    first_char = str1[idx]
    second_char = str2[idx]
    str_sum += ord(first_char) * ord(second_char)

for idx in range(min_len, len(str1)):
    str_sum += ord(str1[idx])

for idx in range(min_len, len(str2)):
    str_sum += ord(str2[idx])

print(str_sum)
