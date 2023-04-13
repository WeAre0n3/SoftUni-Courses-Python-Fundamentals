group_size = int(input())
days = int(input())

coins = 0

for d in range(1, days + 1):

    if d % 15 == 0:
        group_size += 5
    if d % 10 == 0:
        group_size -= 2

    coins += 50 - (2 * group_size)

    if d % 3 == 0:
        coins -= 3 * group_size
    if d % 5 == 0:
        coins += 20 * group_size
    if d % 3 == 0 and d % 5 == 0:
        coins -= 2 * group_size

coins_per_companion = coins // group_size

print(f'{group_size} companions received {coins_per_companion} coins each.')
