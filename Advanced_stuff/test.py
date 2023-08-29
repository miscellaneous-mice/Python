for item in  zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], range(8)):
    print(item)

a = zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], range(8))

print({k : v**2 for k, v in a})

for item in  zip(range(8), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
    print(item)

a = zip(range(8), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print({k : v**2 for v, k in a})

# print({x : x**2 for x in range(10)})