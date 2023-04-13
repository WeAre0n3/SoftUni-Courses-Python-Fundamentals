strings = input().split()

repeated_string = ''

for word in strings:
    length = len(word)
    repeated_string += word * length

print(repeated_string)
