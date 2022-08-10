name = ''
password = ''
array = ['one','two','three']

def passw():
    while True:
        if name != '':
            print('Your name:',name)
            continue
        if password != '':
            continue
        else:
            print("passw() executed successfully.")
            break

def second():
    print('__name__ test.py :', __name__)

def arrayFunction():
    for i in array:
        print('i: ', i)

def prime():
    number = input('Gimme a number: ')
    number = int(number)
    for i in range(2, number):
        if number % i == 0:
            print(number, 'is not a Prime number.')
            break
        else:
            print(number, 'is a Prime number.')
            break

if __name__ == '__main__':
    prime()