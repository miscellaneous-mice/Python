#1
print("One way to print cubes in range 10")
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))

#2
print("\nAnother way to print cubes in range 10")
print([x**3 for x in range(10)])

#3
print("\nUsing map function")
def cubes(n):
    return n**3

print(list(map(lambda num : num**3 , range(10))))

#4
print("\nYield method") # Memory efficient as we don't store anything on memory
def create_cubes_1(n):
    for x in range(n):
        yield (x**3)
    
for y in create_cubes_1(10):  # Here create_cubes_1 is a generator and 
    print(y)

print(create_cubes_1(10)) # Gives generator definition

print(list(create_cubes_1(10))) # You cast the result to a list

#5
print("\nGenerator Fibonacci Sequence")
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a # In real time it yields the result without storing in the memory
        a,b = b,a+b # Here a = b and b = a+b and each iteration a and b changes

for number in gen_fibon(10): # For each number in range(10) yields a result number
    print(number)

#6
print("\nThis is less memory efficient")
def fibon(n):
    a = 1
    b = 1
    output = []
    for i in range(n):
        output.append(a) # In real time we store the value in memory
        a,b = b,a+b # Here a = b and b = a+b and each iteration a and b changes
    return output # After the loop Ends we return the list from the memory
for number in fibon(10): # Here it basically loops through the returned list that was stored in memory
    print(number)


'''
Conclusion (Example 5)
The generator basically yields result in real time without storing in the memory
- In gen_fibbon(n) for every value in 'n' it yields a result a, where 
    a(present) = b(present), 
    b(present) = a(prev)+b(prev)

- Now for number in gen_fibon(10): here it generates result 'number' in real time 
  while looping through the 'gen_fibon' generator. This value isn't stored in memory

- Hence for each loop in for number in gen_fibon(10): a result is generated and
  assigned to 'number', then we print the result 'number' in real time

- Hence in a generator you can find fibonacci for unlimited number's as memory isn't
  constraint it's the processing speed(Calculating cubes)

- In fibon function memory and processing speed is the main constraint
'''

#7
print('\nSimple generator')
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g) # gives the info about the generator

#8
print('\nYield operation manually')
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration: # Informs that all the values have been yielded
    print("Maximum range specified for generator has been reached")
else:
    pass

#9
print("\nIterating through a string using iter")
s = 'hello'
for letter in s: # Here s a string
    print(letter)

try:
    print(next(s))
except TypeError: # Informs that s is not a iterator
    print("'s' is not a iterator function")
else:
    pass

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
'''
Conclusion (Example 7 and 8)
- When the yield operation is called generator basically remembers the previous
  value to generate the next value, and not holding anything in memory

- Yield basically does next(g) operation

- For loop basically print statements like
  next(g)
  next(g)
  |
  |
  |
  next(g)
  till the StopIteration error is thrown

- For loop doesn't have StopIteration error as it catches the error and stops the
  loop sequence i.e., stops executing next(g) code snippet after error
'''

print("\nGenerator Homework")

print("\nCreate a generator that yields 'n' random numbers between a low and high number (that are inputs).")
import random

def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low,high)

for num in rand_num(1, 10, 12):
    print(num)

print("\nGenerator comprehension")
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3) # generator comprehension
listcomp= [item for item in my_list if item > 3] # list comprehension

print(gencomp)
for item in gencomp:
    print(item)


