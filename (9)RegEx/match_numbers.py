import re

nums = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

matches = re.finditer(pattern, nums)

for match in matches:
    print(match.group(), end=' ')
