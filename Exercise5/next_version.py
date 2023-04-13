current_version = [int(x) for x in input().split('.')]

if current_version[2] >= 9:
    current_version[2] = 0
    current_version[1] += 1
    if current_version[1] > 9:
        current_version[1] = 0
        current_version[0] += 1
else:
    current_version[2] += 1

next_version = [str(x) for x in current_version]

print('.'.join(next_version))
