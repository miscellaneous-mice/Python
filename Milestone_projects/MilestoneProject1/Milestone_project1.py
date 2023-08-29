import random

print("simple tic tac toe board")
print("player1 is X and player2 is O")
def display(row1 , row2 , row3):
    print(row1)
    print(row2)
    print(row3)

row1 = ['1 1','1 2','1 3']
row2 = ['2 1','2 2','2 3']
row3 = ['3 1','3 2','3 3']

display(row1 , row2 , row3)

i = random.randint(0,1)
j = 0
a = 'ao'
b = 'bo'

while True:
    if i%2 == 0 :
        XO = ' X '
        x = 1

    else:
        XO = ' O '
        x = 2

    acceptable_range = range(1, 4)
    within_range = False

    while (a.isdigit() == False and b.isdigit() == False) or within_range == False:
        a, b = input(f"Enter row, column for player{x} : ").split()
        if not (a.isdigit() and b.isdigit()):
            print("Sorry that is not a digit!")

        if (a.isdigit() and b.isdigit()):
            if (int(a) in acceptable_range) and (int(b) in acceptable_range):    #accepting values only in the range from 1 to 3
                within_range = True
            else:
                print("hey sorry you are outta acceptable range")
                within_range = False

    a1 = int(a)
    b1 = int(b)-1
    if a1 == 1:
        if (row1[b1] == ' X ') or (row1[b1] == ' O '):
            print("place already occupied")
        else:
            row1[b1] = XO
            #print("oops")
            i = i + 1
    elif a1 == 2:
        if (row2[b1] == ' X ') or (row2[b1] == ' O '):
            print("place already occupied")
        else:
            row2[b1] = XO
            #print("oops")
            i = i + 1
    else:
        if (row3[b1] == ' X ') or (row3[b1] == ' O '):
            print("place already occupied")
        else:
            row3[b1] = XO
            #print("oops")
            i = i + 1

    display(row1 , row2 , row3)
    if row1[0] == row1[1] == row1[2]:
        print(f'victory for player{x}')
        break
    elif row2[0] == row2[1] == row2[2]:
        print(f'victory for player{x}')
        break
    elif row3[0] == row3[1] == row3[2]:
        print(f'victory for player{x}')
        break
    elif row1[0] == row2[1] == row3[2]:
        print(f'victory for player{x}')
        break
    elif row1[2] == row2[1] == row3[0]:
        print(f'victory for player{x}')
        break
    elif row1[0] == row2[0] == row3[0]:
        print(f'victory for player{x}')
        break
    elif row1[1] == row2[1] == row3[1]:
        print(f'victory for player{x}')
        break
    elif row1[2] == row2[2] == row3[2]:
        print(f'victory for player{x}')
        break
    else:
        if j < 8:
            j = j+1
            continue
        else:
            print("Draw :(")
            break







