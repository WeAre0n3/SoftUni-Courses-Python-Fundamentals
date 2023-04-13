friends_list = input().split(', ')

command = input()
blacklisted_names = 0
lost_names = 0

while command != 'Report':
    commands = command.split()
    if commands[0] == 'Blacklist':
        name = commands[1]
        if name in friends_list:
            blacklisted_names += 1
            idx1 = friends_list.index(name)
            friends_list.pop(idx1)
            friends_list.insert(idx1, 'Blacklisted')
            print(f'{name} was blacklisted.')
        else:
            print(f'{name} was not found.')
    elif commands[0] == 'Error':
        idx2 = int(commands[1])
        if 0 <= idx2 < len(friends_list) and friends_list[idx2] != 'Blacklisted' and friends_list[idx2] != 'Lost':
            lost_names += 1
            print(f'{friends_list[idx2]} was lost due to an error.')
            friends_list.pop(idx2)
            friends_list.insert(idx2, 'Lost')
    elif commands[0] == 'Change':
        idx3 = int(commands[1])
        if 0 <= idx3 < len(friends_list):
            print(f'{friends_list[idx3]} changed his username to {commands[2]}.')
            friends_list.pop(idx3)
            friends_list.insert(idx3, commands[2])
    command = input()

print(f'Blacklisted names: {blacklisted_names}')
print(f'Lost names: {lost_names}')
print(' '.join(friends_list))
