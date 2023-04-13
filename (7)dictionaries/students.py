command = input()
students = {}

while ':' in command:
    stats_list = command.split(':')
    name = stats_list[0]
    id = stats_list[1]
    course = stats_list[2]
    if course not in students:
        students[course] = {}

    students[course][id] = name
    command = input()

course = ' '.join(command.split('_'))
for key, value in students.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')
