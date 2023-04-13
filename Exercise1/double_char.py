while True:
    text = input()
    if text == "End":
        break
    elif text == "SoftUni":
        continue
    else:
        for ch in text:
            print(f"{ch}{ch}", end='')

        print()
