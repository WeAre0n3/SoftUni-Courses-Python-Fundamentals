# text = input()
#
# unique_symbols = []
# rage_text = ''
# current_text = ''
#
# for ch in text:
#     if ch.isdigit():
#         rage_text += current_text.upper() * int(ch)
#         current_text = ''
#     else:
#         current_text += ch
#         if ch.upper() not in unique_symbols:
#             unique_symbols.append(ch.upper())
#
# print(f'Unique symbols used: {len(unique_symbols)}')
# print(rage_text)

text = input()

started = False
counter = 0
number = ""
current = ""
result = ""
for i in range(len(text)):
    if started:
        if text[i].isnumeric():
            number += text[i]
        else:
            result += current.lower() * int(number)
            current = ""
            number = ""
            started = False
            if text[i].lower() not in result:
                counter += 1
            current += text[i]

    else:
        if text[i].isnumeric():
            number += text[i]
            started = True
        else:
            if text[i].lower() not in result:
                counter += 1
            current += text[i]

    if i == len(text) - 1:
        result += current.lower() * int(number)

print(f"Unique symbols used: {counter}")
print(result.upper())
