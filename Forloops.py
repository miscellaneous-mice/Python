#loops
mylist = [1,2,3,4,5,6,7,8]
for jelly in mylist:   #you can use any variable name in for '____' in mylist:
    print(jelly)
    print('hello')

#printing even numbers
for num in mylist:
    if (num%2) == 0:
        print(f'even number :{num}')
    else:
        print(f'odd number  :{num}')

#sum of all numbers in list
list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(f'sum of all numbers is :{list_sum}')

mystring = 'hello world'
for letter in mystring:
    print(letter)

#use underscore like 
# for _ in 'hello world'
#      print('cool') prints cool as many words as in hello world

tup = (1,2,3)

for item in tup:
    print(item)

stuff = [(1,2),(3,4),(5,6),(7,8)]
print(len(stuff)) #gives 4 length

print('tuple unpacking')
for (a,b) in stuff: 
    print(a)
    print(b)

print('another tuple unpacking')
mystuff = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mystuff:
    print(b)

print('loops using dictionaries')
d= {'k1':1,'k2':2,'k3':3}
print('key and values')
for items in d.items():
    print(items)

print('printing only keys')
for items in d.keys():
    print(items)

print("printing only values")
for value in d.values():
    print(value)

#break,continue & pass
#pass
x = [1,2,3]
for item in x:
    pass      #to avoid error doesnt do nothing like if you want to print later
print('end of the script') #iouput for the forloop is just this print statement

#continue
myword = 'hello'
for word in myword:
    if word == 'e' :
        continue  #what this does is it continues the loop by going back to loop and continuing process
    print(word)   #only hello is printed out

#break : if you replace continue with break then loops breaks at end



