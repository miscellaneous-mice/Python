x = [1, 2, 3]

x.append([4, 5])

print("List 1 : {}".format(x))

x = [1, 2, 3]

x.extend([4, 5])

print("List 2 : {}".format(x))

l = [1 ,2 ,3 ,4]

l.insert(2, 'inserted') # index, object to insert

print("List 3 : {}".format(l))

# l.pop() # used to pop the last object in the list

l.remove('inserted')

print("List 4 : {}".format(l))

l = [1, 2, 3, 4 ,3]

l.remove(3) # Removes the first instance of 3

print("List 5 : {}".format(l))

