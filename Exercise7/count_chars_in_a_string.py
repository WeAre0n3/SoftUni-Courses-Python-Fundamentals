text = input()
occurrences = {}

for ch in text:
    if ch == ' ':
        pass

    elif ch not in occurrences:
        occurrences[ch] = 1
    else:
        occurrences[ch] += 1

for key, value in occurrences.items():
    print(f'{key} -> {value}')
