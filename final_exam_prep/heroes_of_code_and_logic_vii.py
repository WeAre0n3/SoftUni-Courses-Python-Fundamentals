heroes_num = int(input())

heroes = {}

for _ in range(heroes_num):
    hero = input().split()
    hero_name = hero[0]
    hit_points = int(hero[1])
    mana = int(hero[2])
    heroes[hero_name] = [hit_points, mana]

while True:
    command = input()
    if command == 'End':
        break
    command_args = command.split(' - ')
    if command_args[0] == 'CastSpell':
        name = command_args[1]
        needed_mana = int(command_args[2])
        spell_name = command_args[3]
        if needed_mana <= heroes[name][1]:
            heroes[name][1] -= needed_mana
            print(f'{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

    elif command_args[0] == 'TakeDamage':
        name = command_args[1]
        damage = int(command_args[2])
        attacker = command_args[3]
        heroes[name][0] -= damage
        if heroes[name][0] <= 0:
            heroes.pop(name)
            print(f'{name} has been killed by {attacker}!')
        else:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!')
    elif command_args[0] == 'Recharge':
        name = command_args[1]
        amount = int(command_args[2])
        recharged = 0
        if (heroes[name][1] + amount) > 200:
            recharged = 200 - heroes[name][1]
        else:
            recharged = amount
        heroes[name][1] += recharged
        print(f'{name} recharged for {recharged} MP!')

    elif command_args[0] == 'Heal':
        name = command_args[1]
        amount = int(command_args[2])
        healed = 0
        if (heroes[name][0] + amount) > 100:
            healed = 100 - heroes[name][0]
        else:
            healed = amount
        heroes[name][0] += healed
        print(f'{name} healed for {healed} HP!')

for hero in heroes.keys():
    print(f'{hero}')
    print(f'  HP: {heroes[hero][0]}')
    print(f'  MP: {heroes[hero][1]}')
