def func(): 
    return 1

print(func()) # Calling the function

print(func) # Gives the function definition

def hello():
    return "Hello!"

welcome = hello # Assigning hello function to greet

del hello # Deleting hello

try:
    print(hello()) # Give Error as we've deleted hello function
except NameError:
    print("Hello function is deleted")
else:
    print("The function Hello, Exists!")

print(welcome()) # But greet Exists as we've defined greet as hello

#1
print('\nFirst Example')
def hello(name='Pekka'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is the welcome() function inside hello'

    print(greet())  # Dont return when you just wanna execute function just by calling hello
    print(welcome())

hello()

try:
    print(greet()) # Give Error as we've deleted hello function
except NameError:
    print("Greet function is inside hello and can't be called explicitly outside hello function")
else:
    print("The function greet exists outside hello function")

#2
print('\nConfusion clearing example')
hello_dup = hello # Here its not hello_dup = hello as we don't return any function
hello_dup()

# For another example see workouts.py

#3
print('\nTo make greet executable outside hello function:')
def hello(name='Pekka'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is the welcome() function inside hello'

    print("I am going to return a function!!")
    if name == 'Pekka':
        return greet
    else:
        return welcome

my_new_func = hello('Pekka')

print(my_new_func()) # For another way see workouts.py

#4
print('\nAnother Example:')
def cool():

    def super_cool():
        return 'I am very cool!'
    
    return super_cool

some_func = cool() # This is indirectly some_func = super_cool

print(some_func())

#5
print('\nPassing other function as argument:')
def hello():
    return 'Hi Pekka!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func)

# print(hello)
# other(hello) # Gets the other function definition
other(hello()) # The functionality of the other function is seen

#6
print('\nAnother example:')
def new_decorator(original_func):  # Function 2

    def wrap_func(): # Function 3

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function!')
    
    return wrap_func

def func_needs_decorator(): # Function 1
    print("I want to be decorated!")

# func_needs_decorator() # If you wanna execute this function

decorated_func = new_decorator(func_needs_decorator)
decorated_func() # Function 4

#7
print('\nWith @ operator:')
@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()

'''
Conclusion :
The decorator is used only to (See example 6)
- Take in a function-1

- pass it into a function-2 which has a sub function-3 which expands the functionality
  of the function-1 that is passed as argument to function-2

- return the sub function-3 after expanding the functionality

- Now this return function can be assigned to a another function-4

- This function-4 has expanded functionality i.e. functionality of both
  fucntion-1 and function-3.
  
- We use @function-2 to just add functionality of function-3 into function-1 without 
  need an assignment to another function-4.
'''
