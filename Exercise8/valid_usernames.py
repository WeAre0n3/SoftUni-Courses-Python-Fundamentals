import string

usernames = input().split(', ')

valid_usernames = []

for name in usernames:
    is_invalid = False

    if len(name) < 3 or len(name) > 16:
        is_invalid = True
        continue

    for ch in name:
        if ch in string.ascii_letters or ch in string.digits or ch == '-' or ch == '_':
            continue
        else:
            is_invalid = True
            break

    if not is_invalid:
        valid_usernames.append(name)

for nam in valid_usernames:
    print(nam)
