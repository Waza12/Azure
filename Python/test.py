count = 0

def passw():
    while True:
        name = input('Gimme your name: ')
        if name != '':
            print('Your name:',name)
            continue
        password = input('Gimme your passw: ')
        if password != '':
            continue
        else:
            print("passw() executed successfully.")
            break

def second():
    print('__name__ :', __name__)


if __name__ == '__main__':
    passw()
    second()