words = input().split()

palindrome = input()

list_palindromes = []

for word in words:
    if word == ''.join(reversed(word)):
        list_palindromes.append(word)

print(f'{list_palindromes}')
print(f'Found palindrome {list_palindromes.count(palindrome)} times')
