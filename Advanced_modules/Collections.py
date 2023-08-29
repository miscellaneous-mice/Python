from collections import Counter 

print("Counter Module")
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

print(Counter(mylist))

mylist = ['a', 'a', 'a', 10, 10]
print("\nCounter works for counting strings too")
print(Counter(mylist))

print("\nDirectly passing in a string to Counter")
print(Counter('aaaaaaaaabbbbbbbbbbbshshfdlskfjss'))

sentence = "How many times does each word show up in this sentence with a word"
# print(sentence.lower().split()) # Gives the list of words in sentence
print("\nGives the count of words in a sentence")
print(Counter(sentence.lower().split()))

print("\nCounter is assigned to 'c'")
letters = 'aaaabbbbbbbbbcccccccddddddddddddddd'
c = Counter(letters)
print(c)
print("Most common letters are {}".format(c.most_common()))
print("Most 2 common letters are {}".format(c.most_common(2)))
print("List of Unique values {}".format(list(c)))


from collections import defaultdict

print("\nDefault Dict module")
d = {'a':10}
print("Dictonary d has {}".format(d))
print(d['a'])
# print(d['Wrong']) # Gives error as key isn't present in dictionary d

print("\nCreating default Dictionary")
d = defaultdict(lambda: 0) # Default value is 0
d['correct'] = 100 # Adding 100 to the dictionary d
print(d['correct'])
print(d['wrong'])
print("Dictionary d is {}".format(d))

print("\nStandard tuple")
mytuple = (10, 20, 30)
print(mytuple[0])


from collections import namedtuple

print("\nNamed tuple module")

# Dog is a class which you assign to dog with init parameters age, breed, name
# Then you can access as Dog.age, Dog.breed etc.
dog = namedtuple('Dog', ['age', 'breed', 'name'])
print("Type of Dog object {}".format(dog))

sammy = dog(age=5, breed='Husky', name='Sam')
print("Type of sammy {}".format(type(sammy)))

print(sammy) # We can call this like a class object
print("Sammy's Age {}".format(sammy.age))
print("Sammy's Breed {}".format(sammy.breed))
print("Sammy's nick name {}".format(sammy.name))

print("\nDifferent way of representing this namedtuple")
print("Sammy's Age {}".format(sammy[0]))
print("Sammy's Breed {}".format(sammy[1]))
print("Sammy's nick name {}".format(sammy[2]))


