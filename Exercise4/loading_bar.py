def loading(a):
    loading_bar = []
    for t in range(int(a / 10)):
        loading_bar.append('%')
    for u in range(int(10 - (a / 10))):
        loading_bar.append('.')
    revised_loading_bar = ''.join(loading_bar)

    if a == 100:
        print('100% Complete!')
        print(f'[{revised_loading_bar}]')
    else:
        print(f'{a}% [{revised_loading_bar}]')
        print('Still loading...')


number = int(input())

loading(number)
