x=int(input('Checkered page.\nNumber of rows: '))
y=int(input('Number of columns: '))
def my_chess():
    for m in range(x):
        temp = []
        for n in range(y):
            if (m + n) % 2 == 0:
                temp.append('*')
                print('*', end=' ')
            else:
                print('#', end=' ')
                temp.append('#')
        print()
my_chess()
