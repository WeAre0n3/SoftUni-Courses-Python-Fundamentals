words_and_definitions = input().split(' | ')
dictionary = {}

for word in words_and_definitions:
    divided_word = word.split(': ')
    key = divided_word[0]
    value = divided_word[1]
    if key not in dictionary.keys():
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

words = input().split(' | ')

command = input()

if command == 'Test':
    for word in words:
        if word in dictionary.keys():
            print(f'{word}:')
            for d in dictionary[word]:
                print(f'-{d}')

elif command == 'Hand Over':
    keys = dictionary.keys()
    print(' '.join(keys))
