coffee_counter = 0

while True:
    line = input()

    if line == "END":
        break

    if line == "coding" or line == 'dog' or line == 'cat' or line == 'movie':
        coffee_counter += 1
    elif line == "CODING" or line == 'DOG' or line == 'CAT' or line == 'MOVIE':
        coffee_counter += 2
    else:
        continue

if coffee_counter > 5:
     print("You need extra sleep")
else:
     print(coffee_counter)
