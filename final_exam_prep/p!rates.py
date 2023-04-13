towns = {}

while True:
    command = input()
    if command == 'Sail':
        break
    command_args = command.split('||')
    town = command_args[0]
    population = int(command_args[1])
    gold = int(command_args[2])
    if town not in towns.keys():
        towns[town] = [population, gold]
    else:
        towns[town][0] += population
        towns[town][1] += gold

while True:
    command = input()
    if command == 'End':
        break
    command_args = command.split('=>')
    if command_args[0] == 'Plunder':
        town = command_args[1]
        people = int(command_args[2])
        gold = int(command_args[3])
        towns[town][0] -= people
        towns[town][1] -= gold
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            print(f'{town} has been wiped off the map!')
            del towns[town]
    elif command_args[0] == 'Prosper':
        town = command_args[1]
        gold = int(command_args[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            towns[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {towns[town][1]} gold.')

if len(towns) > 0:
    print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')
    for t in towns.keys():
        print(f'{t} -> Population: {towns[t][0]} citizens, Gold: {towns[t][1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
