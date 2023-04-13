def is_on_the_shelf(book_name):
    if book_name in books:
        return True


books = input().split('&')

command = input()

while command != 'Done':
    commands = command.split(' | ')
    if commands[0] == 'Add Book':
        if is_on_the_shelf(commands[1]):
            pass
        else:
            books.insert(0, commands[1])

    elif commands[0] == 'Take Book':
        if is_on_the_shelf(commands[1]):
            books.remove(commands[1])

    elif commands[0] == 'Swap Books':
        if is_on_the_shelf(commands[1]) and is_on_the_shelf(commands[2]):
            idx1 = books.index(commands[1])
            idx2 = books.index(commands[2])
            books[idx1], books[idx2] = books[idx2], books[idx1]

    elif commands[0] == 'Insert Book':
        if is_on_the_shelf(commands[1]):
            pass
        else:
            books.append(commands[1])

    elif commands[0] == 'Check Book':
        idx = int(commands[1])
        if idx < len(books):
            print(books[idx])

    command = input()

print(', '.join(books))
