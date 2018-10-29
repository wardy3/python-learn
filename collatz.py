start = None

while (start is None):

    start = input('Enter a starting number: ')

    try:
        start = abs(int(start))
    except ValueError:
        print('Please enter a positive integer')
        start = None


def collatz(num):
    if num % 2:
        return 3 * num + 1
    else:
        return num // 2


num = start

while num != 1:
    print(f'Trying num {num}')
    num = collatz(num)
