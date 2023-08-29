import math

# print("Help function to give math module description\n")
# print(help(math))

value = 4.35

print("Rounding off\n")

print("The floor value of 4.35 is: {}".format(math.floor(value)))
print("The ceil value of 4.35 is: {}".format(math.ceil(value)))
print("The round value of 4.35 is: {}".format(round(value)))
# .round() always round of to even values
print("The round value of 4.5 is {} and round value of 5.5 is {}\n".format(round(4.5), round(5.5)))

from math import pi

print("Math values\n")

print("Pi value is {}".format(pi))
print("Infinity value is {}".format(math.inf))
print("Nan value is {}".format(math.nan))
print("Exponential value is {}".format(math.e))
print("loge(e) is  {}".format(math.log(math.e)))
print("log10(100) is  {}".format(math.log(100, 10)))
print("sin(10) is in degrees {}".format(math.sin(10)))
print("pi/2 radians in degrees is {}".format(math.degrees(pi/2)))
print("180 degrees in radians is {}".format(math.radians(180)))
print("sin(pi/2) is in radians {}\n".format(math.sin(pi/2)))

import random

print("Random library\n")
print("Giving 2 random integers within 0 and 100 is : {}, {}".format(
    random.randint(0,100), random.randint(0,100)))

random.seed(42) 
print("Random integer with seed of 42 is: {}".format(random.randint(0,100)))

random.seed(101) 
print("Random integer with seed of 101 is: {}".format(random.randint(0,100)))

random.seed(42)
print("Random integers seed 42: {}, {}, {}, {}, {}".format(random.randint(0,100),
                                                           random.randint(0,100),
                                                           random.randint(0,100),
                                                           random.randint(0,100),
                                                           random.randint(0,100)))

random.seed(42)                                                        
print("Random integers seed 42: {}".format([random.randint(0,100) for _ in range(5)])) 

random.seed(101)                                                       
print("Random integers seed 101: {}, {}, {}, {}, {}".format(random.randint(0,100),
                                                            random.randint(0,100),
                                                            random.randint(0,100),
                                                            random.randint(0,100),
                                                            random.randint(0,100)))

mylist = list(range(0, 20))
random.seed(42)
print("Grabbing random interger from list with seed 42: {}".format(
    random.choice(mylist)))

random.seed(101)
print("Grabbing random interger from list with seed 101: {}".format(
    random.choice(mylist)))

# From here on random.seed is set to 101 as we can see above

# Random numbers grabbed may repeat
print("Grabbing multiple random number from mylist:{}".format(
    random.choices(population=mylist, k=10)))

# Random numbers grabbed doesn't repeat
print("Grabbing multiple random number from mylist:{}".format(
    random.sample(population=mylist, k=10)))

# This will permanently shuffle the list
print("Before Shuffling: {}".format(mylist))
random.shuffle(mylist)
print("After shuffling: {}".format(mylist))

# Uniform distribution meaning: https://www.investopedia.com/terms/u/uniform-distribution.asp
# As Uniform distribution has floating point numbers also
print("Random number from uniform distribution: {}".format(random.uniform(a=0,
b=100)))

# Paramters are centered value and std
print("Random number from Gauss distribution: {}".format(random.gauss(mu=0, 
sigma=1)))