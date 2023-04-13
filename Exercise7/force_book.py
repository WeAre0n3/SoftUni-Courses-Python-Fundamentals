side_by_person = {}
people_by_side = {}


while True:
    line = input()
    if line == 'Lumpawaroo':
        break

    if ' | ' in line:
        command_args = line.split(' | ')
        force_side = command_args[0]
        force_user = command_args[1]

        if force_side not in people_by_side:
            people_by_side[force_side] = []

        if force_user not in side_by_person:
            side_by_person[force_user] = force_side
            people_by_side[force_side].append(force_user)
    else:
        command_args = line.split(' -> ')
        force_user = command_args[0]
        force_side = command_args[1]

        if force_side not in people_by_side:
            people_by_side[force_side] = []

        people_by_side[force_side].append(force_user)
        if force_user in side_by_person:
            old_side = side_by_person[force_user]
            people_by_side[old_side].remove(force_user)
            side_by_person[force_user] = force_side
        else:
            side_by_person[force_user] = force_side

        print(f'{force_user} joins the {force_side} side!')

for side, people in people_by_side.items():
    if len(people) == 0:
        continue
    print(f'Side: {side}, Members: {len(people)}')

    for p in people:
        print(f'! {p}')
