cards = input().split()

cards = set(cards)

team_a = 11
team_b = 11

for c in cards:
    result = c.split('-')
    if result[0] == 'A':
        team_a -= 1
    elif result[0] == 'B':
        team_b -= 1

    if team_a < 7 or team_b < 7:
        break

print(f'Team A - {team_a}; Team B - {team_b}')

if team_a < 7 or team_b < 7:
    print('Game was terminated')
