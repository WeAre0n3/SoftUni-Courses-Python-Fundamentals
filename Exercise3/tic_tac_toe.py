first_line = [int(x) for x in input().split()]
second_line = [int(y) for y in input().split()]
third_line = [int(z) for z in input().split()]

player_one_wins = False
player_two_wins = False

if sum(first_line) == 6 or sum(second_line) == 6 or sum(third_line) == 6:
    player_two_wins = True
elif first_line[0] + second_line[0] + third_line[0] == 6 or first_line[1] + second_line[1] + third_line[1] == 6 or \
        first_line[2] + second_line[2] + third_line[2] == 6:
    player_two_wins = True
elif first_line[0] + second_line[1] + third_line[2] == 6 or first_line[2] + second_line[1] + third_line[2] == 6:
    player_two_wins = True

if first_line[0] == 1 and first_line[1] == 1 and first_line[2] == 1:
    player_one_wins = True
elif second_line[0] == 1 and second_line[1] == 1 and second_line[2] == 1:
    player_one_wins = True
elif third_line[0] == 1 and third_line[1] == 1 and third_line[2] == 1:
    player_one_wins = True
elif first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1:
    player_one_wins = True
elif first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1:
    player_one_wins = True
elif first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1:
    player_one_wins = True
elif first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1:
    player_one_wins = True
elif first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1:
    player_one_wins = True

if player_one_wins:
    print('First player won')
elif player_two_wins:
    print('Second player won')
else:
    print('Draw!')
