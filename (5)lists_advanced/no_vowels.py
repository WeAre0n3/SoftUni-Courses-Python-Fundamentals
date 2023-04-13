forbidden_vowels = ['a', 'o', 'u', 'e', 'i']

result = [ch for ch in input() if ch.lower() not in forbidden_vowels]

print(''.join(result))
