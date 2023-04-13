train = [0] * int(input())

command = input().split()

while command[0] != 'End':
    index = int(command[1])
    if command[0] == 'add':
        train[-1] += index
    elif command[0] == 'insert':
        train[index] += int(command[2])
    elif command[0] == 'leave':
        train[index] -= int(command[2])
    command = input().split()

print(train)
