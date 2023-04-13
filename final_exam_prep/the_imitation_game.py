message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    command_args = command.split('|')
    instruction = command_args[0]
    if instruction == 'Move':
        letters = int(command_args[1])
        message = message[letters:] + message[:letters]
    elif instruction == 'Insert':
        index = int(command_args[1])
        letter = command_args[2]
        message = message[:index] + letter + message[index:]
    elif instruction == 'ChangeAll':
        substring = command_args[1]
        replacement = command_args[2]
        message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')
