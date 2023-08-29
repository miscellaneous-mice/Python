#Booleans
from typing import Text


print(type(False)) #it states it is a boolean
print(1 > 2) #it gives false boolean
print('bye'== 'Bye') #false boolean
print(3!=1) #True

#nested booleans
print(1<2<3)
print(not( ( 1<2 ) and ( 2>3 ) ))

print('first')
mylist = [1,2,3]
for num in range(10):  #prints 0 to 9
    print(num)

print('second')
for num in range(3,10):
    print(num)          #prints 3 to 9

print('third')
for num in range(0,11,2):  #print 0 to 10 in steps of 2
    print(num)

print(list(range(0,11,2)))   #genereate 0 to 10 in steps of 2

#printing index position
index_count = 0
word = 'abcde'
for letter in word:
    print('at index {} the letter is {}'.format(index_count, letter))
    print(word[index_count])   #another way of each string
    index_count += 1

print('enumerate fn')
word_one ='abcde'
for index,letter in enumerate(word_one) : #prints in form(index , word) without index , letter use just item and then print('item')
    print(index) 
    print(letter)
    print('\n')

print('zip function')
mylist1 = [1,2,3,4,5,6]  #even when there is more items in list1 than list2 only till 3 is printed out(i.e. which list is shortest) 
mylist2 = ['a','b','c']
mylist3 = ['100','200','300']
for item in zip(mylist1, mylist2,mylist3):   #zip all lists
    print(item)

print('printing zip in lists format')
print(list(zip(mylist1,mylist2)))

print('checking lists')
print('x' in [1,2,3]) #checks if x is in list
print('a' in 'a world')\

d = {'mykey':345}
print(345 in d.keys()) #if its d.values then it returns true

print('printing min and max values')
yourlist = [1,2,3,4]
print(f'minimum value is {min(yourlist)} and maximum value is {max(yourlist)}')

#importing functions froma library
print('shuffle from random library')
from random import shuffle     #from random library import shuffle function(shuffles the items in list)
newlist = [1,2,3,4,5,6,7]
shuffle(newlist)              #if you put new_list = shuffle(new_list) its not gonna print anything as it is none type
print(newlist)

print('grabbing a random integer')
from random import randint
new_num = randint(0,100)      
print(new_num)

print('input from user')
myresult = input('whats your name : ')  #always accepts input as string not as int etc
print(f'your name is {myresult}')

#to convert your string type from input function to float do bottom codes
#float(result) 
#int(result)

print('accepting integers')
new_result = int(input('Favorite no. : '))
print(f'Your favorite number is {new_result}')











