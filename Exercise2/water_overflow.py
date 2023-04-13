n = int(input())

total_capacity = 255
current_volume = 0

for i in range(n):
    liters_of_water = int(input())
    current_volume += liters_of_water

    if current_volume > total_capacity:
        print('Insufficient capacity!')
        current_volume -= liters_of_water
        continue

print(current_volume)
