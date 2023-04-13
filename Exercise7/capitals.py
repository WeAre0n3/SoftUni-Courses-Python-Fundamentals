countries = input().split(', ')
capitals = input().split(', ')

dictionary = {countries[idx]: capitals[idx] for idx in range(len(countries))}

for key, value in dictionary.items():
    print(f'{key} -> {value}')
