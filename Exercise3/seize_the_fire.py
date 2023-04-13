level_of_fire = input().split('#')

amount_water = int(input())

cells = []
total_effort = 0

total_fire = 0
for fire in level_of_fire:
    cell = fire.split(' = ')
    type_of_fire = cell[0]
    range_fire = int(cell[1])

    if type_of_fire == 'High' and 81 <= range_fire <= 125:
        if amount_water < range_fire:
            continue
        amount_water -= range_fire
        cells.append(range_fire)
        total_effort += range_fire * 0.25
        total_fire += range_fire
    elif type_of_fire == 'Medium' and 51 <= range_fire <= 80:
        if amount_water < range_fire:
            continue
        amount_water -= range_fire
        cells.append(range_fire)
        total_effort += range_fire * 0.25
        total_fire += range_fire
    elif type_of_fire == 'Low' and 1 <= range_fire <= 50:
        if amount_water < range_fire:
            continue
        amount_water -= range_fire
        cells.append(range_fire)
        total_effort += range_fire * 0.25
        total_fire += range_fire

print(f'Cells: ')
for c in cells:
    print(f' - {c}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
