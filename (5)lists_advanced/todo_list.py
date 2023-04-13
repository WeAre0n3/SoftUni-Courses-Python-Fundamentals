todo_notes = input()

todo_list = [0] * 10

while todo_notes != 'End':
    command_list = todo_notes.split('-')
    importance = int(command_list[0]) - 1
    todo_list[importance] = command_list[1]
    todo_notes = input()

print([el for el in todo_list if el != 0])
