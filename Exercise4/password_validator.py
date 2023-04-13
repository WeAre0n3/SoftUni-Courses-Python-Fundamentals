def is_pass_valid(a):
    is_valid = True
    if len(a) < 6 or len(a) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    nums_count = 0
    for ch in a:
        if 48 <= ord(ch) <= 57 or 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            pass
        else:
            is_valid = False
            print("Password must consist only of letters and digits")
            break
        if 48 <= ord(ch) <= 57:
            nums_count += 1
    if nums_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()

is_pass_valid(password)
