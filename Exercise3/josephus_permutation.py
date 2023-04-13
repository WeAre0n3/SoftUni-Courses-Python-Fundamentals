circle = input().split(' ')

k = int(input())

result = []

counter = 0
index = 0

while len(circle) > 0:
    counter += 1

    if counter % k == 0:
        result.append(circle.pop(index))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))
