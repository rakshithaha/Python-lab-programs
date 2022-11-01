a=int(input('Enter the number of rows'))
for i in range(a):
        for j in range(a-i):
            print('*', end='')
        print('\n')
