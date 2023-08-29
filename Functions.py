def say_hello(name = 'Who are you'): 
    print(f'Hello! {name}')

say_hello('jose')

print('adding 2 numbers using return type function')
def add_num(num1,num2):  #return type
    return num1 + num2  #only return saves value not print to later assign to some other variable
result = add_num(1,2)
print(result)

print('adding two numbers using print type function')
def print_add(no1,no2): 
    print(no1+no2)
print_add(10,20)

print('using return and print to add')
def myfunc(a,b): 
    print(a + b)
    return a + b
myfunc(10,200)

print('checks if even no. using functions')

def even_check(a):
    return a%2 == 0
print(even_check(10))

print('to pick all the even numbers from the list')
def list_even(num_list):
    even_list = []
    for number in num_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass  #if you put return False here then forloop ends once odd number is in first place itself
    return even_list
numlist = [1,2,5,6,9]
print(list_even(numlist))

print('tuple unpacking')

work_hours = [('abby',100),('billy',400),('cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

name , hours = employee_check(work_hours)  #tuple unpacking
print(f'{name} is employee of year with {hours} hours of work')


print('random module')
example = [1,2,3,4,5,6,7]
from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(example)
print(f'shuffled list is{result}')

print('\n')
print('lets play a game')

def player_guess():
    guess = ''

    while guess not in ['1','2','3']:
        guess = input("which position does the 'o' lie in after shuffling: 1, 2 or 3 : ")
        guess1 = int(guess) - 1

    return guess1  #return as int as input always returns as string


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('correct')
        print(f'the list is \n{mylist}')
    else:
        print('wrong guess!')
        print(f'the correct answer is \n{mylist}')

#initial list
my_list = [' ','O',' ']
print(f"the 'O' is in this position initially {my_list}")

#shuffle list
mixedup_list = shuffle_list(my_list)

#user guess
guess = player_guess()

#check guess
check_guess(mixedup_list,guess)

print('danke for playing')


