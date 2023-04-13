gifts = input().split()
line = input()
while line != "No Money":
    command_args = line.split(" ")
    command = command_args[0]
    gift = command_args[1]

    if command == "OutOfStock":
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"

    elif command == "Required":
        idx = int(command_args[2])
        if 0 <= idx < len(gifts):  # is exclusive because len -1
            gifts[idx] = gift

    elif command == "JustInCase":
        gifts[-1] = gift  # gift[-1] is short syntax for the last element

    line = input()

for gift in gifts:
    if gift == "None":
        pass
    else:
        print(gift, end=" ")
