activation_key = input()

while True:
    command = input()
    if command == 'Generate':
        break

    command_args = command.split('>>>')
    if command_args[0] == 'Contains':
        substring = command_args[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif command_args[0] == 'Flip':
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if command_args[1] == 'Lower':
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() +\
                             activation_key[end_index:]

        else:
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + \
                             activation_key[end_index:]
        print(activation_key)

    elif command_args[0] == 'Slice':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f'Your activation key is: {activation_key}')
