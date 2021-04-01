import random
import time
from termcolor import cprint


def elapsed_time():
    end = time.time()
    elapsed = end - start
    print("elapsed time: ", elapsed)
    exit()

def my_tic():
    for m in range(3):
        for n in range(3):
            if game[m][n] == 'x':
                cprint('x', 'magenta', end=' ')
            elif game[m][n] == '0':
                cprint('x', 'blue', end=' ')
            else:
                print(game[m][n], end=' ')
        print()
        pass


def barandeh():
    if game[0][0]=='x' and game[0][1]=='x' and game[0][2]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[1][0]=='x' and game[1][1]=='x' and game[1][2]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[2][0]=='x' and game[2][1]=='x' and game[2][2]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[0][0]=='x' and game[1][0]=='x' and game[2][0]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[0][1] == 'x' and game[1][1] == 'x' and game[2][1]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[0][2]=='x' and game[1][2]=='x' and game[2][2]=='x':
        print('player1 wins')
        elapsed_time()
    elif game[0][0] == 'o' and game[0][1] == 'o' and game[0][2] == 'o':
        print('player2 wins')
        elapsed_time()
    elif game[1][0] == 'o' and game[1][1] == 'o' and game[1][2] == 'o':
        print('player2 wins')
        elapsed_time()
    elif game[2][0]=='o' and game[2][1]=='o' and game[2][2]=='o':
        print('player2 wins')
        elapsed_time()
    elif game[0][0] == 'o' and game[1][0] == 'o' and game[2][0]=='o':
        print('player2 wins')
        elapsed_time()
    elif game[0][1] == 'o' and game[1][1] == 'o' and game[2][1]=='o':
        print('player2 wins')
        elapsed_time()
    elif game[0][2] == 'o' and game[1][2] == 'o' and game[2][2]=='o':
        print('player2 wins')
        elapsed_time()

    elif sum([row.count('-') for row in game]) == 0:
        print('draw')
        elapsed_time()



def player():
    my_tic()
    while True:
        while True:
            #player1
            print('player1')
            row=int(input('Enter the row:'))
            col=int(input('Enter the column:'))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]=='-':
                    game[row][col]='x'
                    my_tic()
                    barandeh()
                    break
                else:
                    print('no empty')
            else:
                print('error!')

        while True:
            #player 2
            print('player 2')
            row=int(input('Enter the row:'))
            col=int(input('Enter the column:'))
            if 0<=row<=2 and 0<=col<=2:
                if game[row][col]=='-':
                    game[row][col]='o'
                    my_tic()
                    barandeh()
                    break
                else:
                    print('no empty')
            else:
                print('error!')

def tak():
    while True:

        while True:
            print('player1')
            row =random.randint(0,2)
            col =random.randint(0,2)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game[row][col] == '-':
                    game[row][col] = 'x'
                    my_tic()
                    barandeh()
                    break
                else:
                    print('no empty')
            else:
                print('error!')

        while True:
            print('player 2')
            row=int(input('Enter the row:'))
            col=int(input('Enter the column:'))
            if 0<=row<=2 or 0<=col<=2:
                if game[row][col]=='-':
                    game[row][col]='o'
                    my_tic()
                    barandeh()
                    break
                else:
                    print('no empty')
            else:
                print('error!')

start=time.time()
game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]


my_tic()
number=int(input('Select game start mode: \n1 players 2 players\n'))
if number==1:
    tak()
if number==2:
    player()
