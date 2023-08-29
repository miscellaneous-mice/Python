my_list = ['mike','testing','excuse me'] 
print(len(my_list)) #no. of objcets 
print(my_list[0]) #to grab a object
print(my_list[1:]) #to print all objects from 2nd object i.e. 'testing'
another_list = ['one','two','three']
new_list = another_list + my_list
print(new_list) #concatinaed list
new_list[0] = 'ONE' #to replace one with ONE
new_list.append('four') #to add four at end of list
print(new_list)
new_list.pop() #to remove object from end of list
print(new_list)
popped_item = new_list.pop() 
print(popped_item)
new_list.pop(2) #to pop item from a particular location in the list
#you can even use new_list.pop(-1) to remove end of list
print(new_list)
newlist = ['e','b','d','c','a']
numlist = [4,1,8,3]
newlist.sort() #to sort list
#my_sorted_list = newlist.sort() will give no value if you print(my_sorted_list)
my_sorted_list = newlist
print(my_sorted_list)  #now you will get value
numlist.reverse() #to reverse list
print(numlist)

#DICTIONARIES

#to retreive the key value pair to find a object in the list 
#you cannot sort etc in dictionaries but lists have tho
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
prices_lookup = {'apple':2.99,'oranges':1.99, 'milk':5.80}
print(prices_lookup['apple'])
d= {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}} #different type of using dictionaries
print(d['k3']['insideKey'])
d = {'key1':['a','b','c']}
#1 mylist = d['key1'] 
#2 letter = mylist[2] 
#3 letter.upper() 
#4 print(letter)
print(d['key1'][2].upper()) #instead of doing 1,2,3 & 4
d = {'k1':100, 'k2': 200}
d['k3'] = 300 #adding new key value pair 
d['k1'] = 'new value' #replacing 1st object in dictionary
print(d.keys()) #returns all the keys 
print(d.values()) #returns all the value of keys
print(d.items()) #returns keys and keys values


#List comprehensions
print('making list of every character in a string')
mystring = 'hello'
list_my = []

for letter in mystring:
    list_my.append(letter)
print(list_my)


print('better way of implementation')
list_my = [letter.lower() for letter in mystring]
print(list_my)

print("another example")
print([word for word in 'hello world'])

print("another example")
print([num for num in range(0,11)])
print(f'square of numbers is {[num**2 for num in range(0,11)]}')
print(f'square of even numbers in list is{[x**2 for x in range(0,11) if x%2 ==0]}')

print('celcius to farenheit')
celcius = [15,25,30,35,45,48]
print(f'temp in fahrenheit is {[float(((9/5)*temp +32)) for temp in celcius]}')


print('if else statements in list')
# results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]
results = ['EVEN' if x%2 == 0 else 'ODD' for x in range(0,11)]
print(results)

print('nested loop in list comprehension')
list_nested = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        list_nested.append(x*y)
print(list_nested)

#in comprehensive manner
# nestedlist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(f'nested list is : {[x*y for x in [2,4,6] for y in [1,10,1000]]}')

