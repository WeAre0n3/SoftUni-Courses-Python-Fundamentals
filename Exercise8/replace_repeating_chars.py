text = input()

redacted_text = ''
previous_letter = ''
for letter in text:
    if letter == previous_letter:
        continue
    else:
        redacted_text += letter

    previous_letter = letter

print(redacted_text)
