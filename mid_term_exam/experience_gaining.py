total_xp_needed = float(input())
total_xp_gained = 0
battles_count = int(input())
num_battles = 0

for b in range(1, battles_count + 1):
    if total_xp_gained >= total_xp_needed:
        break
    num_battles += 1
    xp_gained = float(input())
    if b % 3 == 0:
        total_xp_gained += xp_gained + (xp_gained * 0.15)
    elif b % 5 == 0:
        total_xp_gained += xp_gained - (xp_gained * 0.10)
    elif b % 15 == 0:
        total_xp_gained += xp_gained + (xp_gained * 0.05)
    else:
        total_xp_gained += xp_gained

if total_xp_gained >= total_xp_needed:
    print(f'Player successfully collected his needed experience for {num_battles} battles.')
else:
    needed_xp = total_xp_needed - total_xp_gained
    print(f'Player was not able to collect the needed experience, {needed_xp:.2f} more needed.')
