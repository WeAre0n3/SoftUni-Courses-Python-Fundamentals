import random

names = ["Peter", "Michell", "Jane", "Steve", "Stan"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings", "throws"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "in space"]


def get_random_word(words):
    return random.choice(words)


print('Hello, click [Enter] to generate your first random sentence:')
user_input = input()

while user_input == '':
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f'{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}')
    print('Click [Enter] to generate a new one.')
    user_input = input()
