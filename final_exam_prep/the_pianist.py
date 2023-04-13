initial_num = int(input())

stored_music = {}

for _ in range(initial_num):
    music_piece = input().split('|')
    piece = music_piece[0]
    composer = music_piece[1]
    key = music_piece[2]
    stored_music[piece] = [composer, key]

while True:
    command = input()
    if command == 'Stop':
        break
    command_args = command.split('|')

    if command_args[0] == 'Add':
        piece = command_args[1]
        composer = command_args[2]
        key = command_args[3]
        if piece in stored_music.keys():
            print(f'{piece} is already in the collection!')
        else:
            stored_music[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')

    elif command_args[0] == 'Remove':
        piece = command_args[1]
        if piece in stored_music.keys():
            stored_music.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif command_args[0] == 'ChangeKey':
        piece = command_args[1]
        new_key = command_args[2]
        if piece in stored_music.keys():
            stored_music[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')


for p in stored_music.keys():
    print(f'{p} -> Composer: {stored_music[p][0]}, Key: {stored_music[p][1]}')
