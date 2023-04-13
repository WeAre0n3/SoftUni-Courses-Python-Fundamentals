text = input()

encrypted_text = ''

for ch in text:
    encrypted_ch_value = ord(ch) + 3
    encrypted_text += chr(encrypted_ch_value)

print(encrypted_text)
