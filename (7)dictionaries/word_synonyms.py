synonyms = {}

number = int(input())

for n in range(1, number + 1):
    key_word = input()
    synonym_value = input()
    if key_word not in synonyms:
        synonyms[key_word] = [synonym_value]
    else:
        synonyms[key_word].append(synonym_value)

for keys in synonyms.keys():
    print(f'{keys} - {", ".join(synonyms[keys])}')
