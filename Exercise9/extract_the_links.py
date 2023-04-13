import re

emails = []
while True:
    text = input()
    if not text:
        break

    matches = re.findall(r'(www.[A-Za-z\d\-]+(\.[A-Za-z]+)+)', text)
    emails.extend(m[0] for m in matches)

for email in emails:
    print(email)
