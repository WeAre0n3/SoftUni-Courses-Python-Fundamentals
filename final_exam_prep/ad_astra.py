import re

text = input()

pattern = r'(#|\|)(?P<Item>[A-Za-z]+ ?[A-Za-z]+)\1(?P<Date>\d\d\/\d\d\/\d\d)\1(?P<Calories>\d+)\1'
results = re.findall(pattern, text)

items = []
exp_dates = []
calories = []
total_calories = 0

for result in results:
    item = result[1]
    exp_date = result[2]
    calories_value = int(result[3])
    items.append(item)
    exp_dates.append(exp_date)
    calories.append(calories_value)
    total_calories += calories_value

days_to_live = total_calories // 2000

print(f'You have food to last you for: {days_to_live} days!')

for i in range(len(items)):
    print(f'Item: {items[i]}, Best before: {exp_dates[i]}, Nutrition: {calories[i]}')
