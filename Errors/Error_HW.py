try:
    for i in ['a','b','c']:
        print(i ** 2)
except TypeError:
    print("looks like you arent squaring numbers properly i.e. type error")
except:
    print("all other exceptions")
else:
    print("Above program went well")

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("looks like you are dividing by zero")
except:
    print("all other exceptions")
else:
    print("Above program went well")
    print(z)
