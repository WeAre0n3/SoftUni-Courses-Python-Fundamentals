rooms = int(input())

room_num = 1
free_chairs = True
chairs = 0
for r in range(rooms):
    chair_info = input().split()
    if len(chair_info[0]) < int(chair_info[1]):
        print(f'{int(chair_info[1]) - len(chair_info[0])} more chairs needed in room {room_num}')
        free_chairs = False
    else:
        chairs += len(chair_info[0]) - int(chair_info[1])
    room_num += 1

if free_chairs:
    print(f'Game On, {chairs} free chairs left')
