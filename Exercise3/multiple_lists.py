factor = int(input())
count = int(input())

num_list = []

counter = 1
for n in range(count):
    num_list.append(factor * counter)
    counter += 1

print(num_list)
