words_list = [x for x in input().split() if len(x) % 2 == 0]

print(*words_list, sep='\n')
