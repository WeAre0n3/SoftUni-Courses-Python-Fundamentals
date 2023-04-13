number = int(input())

for n in range(number):
    text = input()
    is_pure = True
    for ch in text:
        if ch == "," or ch == "." or ch == "_":
            is_pure = False
            break
    if is_pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
