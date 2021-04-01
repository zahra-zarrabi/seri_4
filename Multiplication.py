x=int(input('Multiplication table:\n Number of rows: '))
y=int(input('Number of columns:'))
def my_mult():
    for n in range(1, x+1):
        for m in range(1, y+1):
            print(n*m, end=' ')
        print()

my_mult()