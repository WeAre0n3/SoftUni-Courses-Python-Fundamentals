spell = input()

while True:
    command = input()
    if command == 'Abracadabra':
        break

    command_args = command.split()

    if command_args[0] == 'Abjuration':
        spell = spell.upper()
        print(spell)

    elif command_args[0] == 'Necromancy':
        spell = spell.lower()
        print(spell)

    elif command_args[0] == 'Illusion':
        index = int(command_args[1])
        letter = command_args[2]
        if index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print('Done!')
        else:
            print('The spell was too weak.')

    elif command_args[0] == 'Divination':
        first_substring = command_args[1]
        second_substring = command_args[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif command_args[0] == 'Alteration':
        substring = command_args[1]
        if substring in spell:
            spell = spell.replace(substring, '')
            print(spell)
    else:
        print('The spell did not work!')
