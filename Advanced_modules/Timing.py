def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str, range(10)))

print(func_two(10))

import time
print("Time module for 1000000 numbers")
# Starting the timing
start_time = time.time()

# Running the function
result = func_one(1000000)

# Stops the time when function is executed
end_time = time.time()

# Calulates the time it took to execute an function
elapsed_time = end_time - start_time
print("Time it took to execute func_one is {}".format(elapsed_time))

# Starting the timing
start_time = time.time()

# Running the function
result = func_two(1000000)

# Stops the time when function is executed
end_time = time.time()

# Calulates the time it took to execute an function
elapsed_time = end_time - start_time
print("Time it took to execute func_two is {}".format(elapsed_time))

print("Time module for 10000 numbers") # Gives inaccurate results

start_time = time.time()
result = func_one(10000)
end_time = time.time()
elapsed_time = end_time - start_time
print("Time it took to execute func_one is {}".format(elapsed_time))

start_time = time.time()
result = func_two(10000)
elapsed_time = time.time() - start_time
print("Time it took to execute func_two is {}".format(elapsed_time))

print("\nTimeit module")
import timeit

print("\nTimeit module for function 1")
stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number = 100000))


print("Timeit module for function 2")
stmt = '''
func_two(100)
'''

setup = '''
def func_two(n):
    return list(map(str, range(10)))
'''

print(timeit.timeit(stmt, setup, number = 100000))

print("Timeit module for generators")
stmt = '''
list(gen_func(100))
'''

setup = '''
def gen_func(n):
    for i in range(n):
        yield n
'''

print(timeit.timeit(stmt, setup, number = 100000))

print("\nTimeit module for searching")
stmt = '''
text = "The agent's phone number is 408-555-1234. Call soon!"
'phone' in text
'''

setup = '''
'''

print(timeit.timeit(stmt, setup, number = 100000))

print("Timeit module for regex")
stmt = '''
text = "The agent's phone number is 408-555-1234. Call soon!"
re.search('phone', text)
'''

setup = '''
import re
'''

print(timeit.timeit(stmt, setup, number = 100000))