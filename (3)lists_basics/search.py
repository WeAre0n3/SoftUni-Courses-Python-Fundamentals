n = int(input())
word = input()

strings = []
strings_with_word = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)
    if word in current_string:
        strings_with_word.append(current_string)

print(strings)
print(strings_with_word)
