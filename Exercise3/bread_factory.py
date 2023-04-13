init_energy = 100
init_coins = 100

working_events = input().split('|')

for w in working_events:
    event = w.split('-')
    event_name = event[0]
    number = int(event[1])

    if event_name == 'rest':
        if init_energy == 100:
            gained_energy = 0
        else:
            gained_energy = number
            init_energy += gained_energy

        if init_energy > 100:
            remainder = init_energy - 100
            gained_energy -= remainder
            init_energy = 100

        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {init_energy}.')

    elif event_name == 'order':
        if init_energy >= 30:
            init_energy -= 30
            init_coins += number
            print(f'You earned {number} coins.')
        else:
            init_energy += 50
            print('You had to rest!')

    else:
        if init_coins >= number:
            init_coins -= number
            print(f'You bought {event_name}.')
        else:
            print(f'Closed! Cannot afford {event_name}.')
            quit()

print('Day completed!')
print(f'Coins: {init_coins}')
print(f'Energy: {init_energy}')
