num_sequence = [int(x) for x in input().split()]

laps = int((len(num_sequence) - 1) / 2)

left_racer = num_sequence[0:laps]
right_racer = num_sequence[laps + 1:]
right_racer.reverse()
total_time_left = 0
total_time_right = 0

for l in left_racer:
    if l == 0:
        total_time_left -= total_time_left * 0.20
    else:
        total_time_left += l

for m in right_racer:
    if m == 0:
        total_time_right -= total_time_right * 0.20
    else:
        total_time_right += m

if total_time_left > total_time_right:
    print(f'The winner is right with total time: {total_time_right:.1f}')
elif total_time_right > total_time_left:
    print(f'The winner is left with total time: {total_time_left:.1f}')
