def ascii_range(a, b):
    for ch in range(a + 1, b):
        print(chr(ch), end=' ')


first_char = ord(input())
second_char = ord(input())

ascii_range(first_char, second_char)
