password = input()
modified_pass = ''

while True:
    command = input()
    if command == 'Done':
        break
    command_args = command.split()

    if command_args[0] == 'TakeOdd':
        for symbol in range(len(password)):
            if symbol % 2 != 0:
                modified_pass += password[symbol]
        password = modified_pass
        print(password)
    elif command_args[0] == 'Cut':
        index = int(command_args[1])
        length = int(command_args[2])
        string_to_remove = password[index:index + length]
        password = password.replace(string_to_remove, '', 1)
        print(password)
    elif command_args[0] == 'Substitute':
        substring = command_args[1]
        substitute = command_args[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')

print(f'Your password is: {password}')
