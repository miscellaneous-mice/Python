#if, elseif
hungry = True
if hungry:
    print("im hungry")
else:
    print('im not hungry')
#checking strings
loc = 'bank'
if loc == 'autoshop':
    print('cars are cool')
else:
    print('dont know place')

#elif statement
place = 'store'

if place =='autoshop':
    print('cars are here')
elif place == 'bank':
    print('money here')
elif place == 'store':
    print('happy shopping')
else:
    print('dont know much')

print('to check if a object is there or not in the list')
def blackjack(a,b,c):
    if 11 in [a,b,c]:
        print('found 11')
    else:
        print('no eleven')

blackjack(3,9,10)
