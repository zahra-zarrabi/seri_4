x=int(input('Checkered page.\nNumber of rows: '))
y=int(input('Number of columns: '))
def my_chess():
    for n in range(x+1):
        print()
        for m in range(y+1):
            n='#'
            m='*'
            print(n , m , end=' ')
my_chess()
