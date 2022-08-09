count = 0
while True:
    name = input('Gimme your name: ')
    if name != 'lol':
        print('Your name:',name)
        continue
    password = input('Gimme your passw: ')
    if password != 'meh':
        continue
    else:
        print("Welcum.")
        break