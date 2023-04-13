phone = input()

phonebook = {}

while '-' in phone:
    phones_list = phone.split('-')
    name = phones_list[0]
    number = phones_list[1]
    phonebook[name] = number
    phone = input()

phone = int(phone)

for _ in range(1, phone + 1):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
