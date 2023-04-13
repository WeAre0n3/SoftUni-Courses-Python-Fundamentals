snowballs = int(input())

best_snowball = float('-inf')
output = ''

for s in range(snowballs):
    weight = int(input())
    travel_time = int(input())
    quality = int(input())
    snowball_value = (weight // travel_time) ** quality
    if snowball_value > best_snowball:
        best_snowball = snowball_value
        output = f'{weight} : {travel_time} = {snowball_value} ({quality})'

print(output)
