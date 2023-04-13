str_1 = input().split(', ')
str_2 = input().split(', ')

substrings = []

for s in str_1:
    for t in str_2:
        if s in t:
            if s in substrings:
                continue
            else:
                substrings.append(s)

print(substrings)
