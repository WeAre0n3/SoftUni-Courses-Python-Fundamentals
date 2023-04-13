import re

match_list = []
while True:
    text = input()
    if not text:
        break
    matches = re.findall('\\d+', text)
    match_list.extend(matches)

print(' '.join(match_list))
