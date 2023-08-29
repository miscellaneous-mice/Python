d = {'k1':1, 'k2':2}

# Creating dictionaries through dictionary comprehension
print("Dict 1 : {}".format({x : x**2 for x in range(10)}))

# See test.py for below code
print("Dict 2 : {}".format({k : v**2 for k, v in zip(['a', 'b'], range(2))}))

print("Dict 3 : ")
for k in d.items():
    print(k)

for k in d.values():
    print(k)

for k in d.keys():
    print(k)

print("Dict 4 : {}".format(d.items()))

print("Dict 5 : {}".format(d.keys()))

print("Dict 6 : {}".format(d.values()))