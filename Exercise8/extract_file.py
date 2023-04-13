file_path = input().split('\\')

name_extension = file_path[-1].split('.')

file_name = name_extension[0]
file_ext = name_extension[1]

print(f'File name: {file_name}')
print(f'File extension: {file_ext}')
