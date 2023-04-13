import re

text = input()

coolness_threshold = 1
for t in text:
    if t.isdigit():
        coolness_threshold *= int(t)

print(f'Cool threshold: {coolness_threshold}')

pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'

matches = re.findall(pattern, text)
num_matches = len(matches)

print(f'{num_matches} emojis found in the text. The cool ones are:')

for match in matches:
    word = match[1]
    symbols = match[0]
    is_word_cool = 0
    for l in word:
        is_word_cool += ord(l)
    if is_word_cool >= coolness_threshold:
        print(f'{symbols}{word}{symbols}')
