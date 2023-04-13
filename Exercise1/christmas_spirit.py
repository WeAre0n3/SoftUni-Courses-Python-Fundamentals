num_decorations = int(input())
days_left = int(input())

cost = 0
christmas_spirit = 0

for d in range(1, days_left + 1):
    if d % 11 == 0:
        num_decorations += 2
    if d % 2 == 0:
        cost += (2 * num_decorations)
        christmas_spirit += 5
    if d % 3 == 0:
        cost += (8 * num_decorations)
        christmas_spirit += 13
    if d % 5 == 0:
        cost += (15 * num_decorations)
        christmas_spirit += 17
    if d % 3 == 0 and d % 5 == 0:
        christmas_spirit += 30
    if d % 10 == 0:
        cost += 23
        christmas_spirit -= 20

if days_left % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")
