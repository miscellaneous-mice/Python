from re import X

def myfunction(a,b,c=0,d=0):  #you assign these variables = 0 if user doesnt use these variables it doesnt give error
    #returns 5% of sum of a and b
    return sum((a,b,c,d))*0.05

print(myfunction(10,40,5))

print('instead of above assigning many variables')
def myfunc(*args): #now you can assign as many variables as you want if you use that '*' before variable
    print(f'returns a tuple {args}')
    for item in args:
        print(item)
#treats as tuples in the function
print(myfunc(1,2,3,4)) #you can add how many numbers as you want

def my_func(**kwrgs): 
    print(f'its a dictionary {kwrgs} ')
    for item in kwrgs:
#        if 'fruit' in kwrgs:
#            print('my fruit of choice is {}'.format(kwrgs['fruit']))
#        else:
#            print('none of my choice here')
        print(f"my {item} of choice is {kwrgs[item]} ")
#returns dictionary

my_func(fruit = 'apple', veggie = 'lettuce')

print('combination of arguments and keyword arguments')

def my_function(*arg, **kwargs):
    i = 0
    print(arg)
    print(kwargs)
    for stuff in kwargs:
        print('i would like {} {} '.format(arg[i], kwargs[stuff]))
        i = i+1

my_function(10,20,30, fruit = 'oranges', veggie = 'carrot', food = 'eggs')


#lambda expressions
print('\n')
print('map function')
def square(num):
    return num**2

mynum = [1,2,3,4,5]

print(list(map(square,mynum)))


print('\n')
print('another example')
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring

names = ['andy','sam','sally']
print(list(map(splicer,names)))

#so basically map just iterates all variables from the list through to function to get the result
print('\n')
print('filter function')
# def check_even(a):
#     if a%2 == 0:
#         return True
#     else:
#         return False

def check_even(a):
    return (a%2 == 0)

list_num = [1,2,3,4,5]
print(list(filter(check_even,list_num)))
#print(list(map(check_even,list_num)))

#for n in filter(check_even,list_num):      #to iterate through all the variables
    #print(n)

#filter basically picks numbers from list based on the condition in the function

print('\n')
print('lambda function')
square = lambda num : num**2 #simplify to simplest form you can 
print(square(2))

print('using lambda with map functions')
mynums = [1,2,3,4,5]
print(list(map(lambda num : num**2 , mynums )))

print('using lambda with filter function')
print(list(filter(lambda num : num%2 ==0 , mynums)))

print('getting reversing of every string in the list')
print(list(map(lambda x : x[::-1],names)))

print('\n')
print('printing')
x = 25
def printer():
    x= 50
    return X
print(printer())
#see LEGB rule in nested statements and scopes at 2:40

print('\n')
name = 'this is a global string'
def greet():
    name = 'sammy'       #if you comment this out then you will get : hello this is a global string
    def hello():
        name = 'im a local'    #if you comment this out then you will be obtained with : hello sammy
        print('Hello '+name)
    hello()
greet()

#selects which string is used in print based of LEGB rule
print('\n')
print('printing global or local variables on command')
y = 60 
def fucn(y):
    print(f'X is {y}')
    y = 200        #local reassignment
    print(f'i just changed x to {y}')
fucn(y)
print(f'original value is {y}')

x = 50

print('\n')
print('global variables')
def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
#to do a local assignment to x we instead put x = fucn(x) in line 117 so that x is not globally altered see lec 56 14:30

print('\n')
print('to check lower case and uppercase letters')
#to check better version of the solution using dictionaries check the module in method.py
def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass  #if there is question mark or special characters
    print(f'the original string is {s}')
    print(f'the number of uppercase letters are {uppercase}')
    print(f' the number of lowercase letters are {lowercase}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

print('\n')
print('to replace characters in the string')
s = 'how are you doing?'
s = s.replace('o','-')
print(s)