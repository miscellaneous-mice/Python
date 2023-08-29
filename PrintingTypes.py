print('hello')
print("i'm weird") 
print('hello\tworld') #escape sequence
b = 10
print(type(b)) #type of variable is it a int or float etc


#STRINGS
mystring = "hello world"
print(mystring[0])
print(mystring[-2]) #grabing a character from string
print(mystring[6:]) #slicing from character 2 to end
print(mystring[:5]) #slicing from start to character 5 i.e 'o'

print(mystring[2:8]) #slicing or grab middle part of string
print(mystring[2:10:2]) #[start:stop:stepsizejump]
print(mystring[::-1]) # reversing string

name = "Sam"
name = name[1:] #assigning last 2 letters to this variable
print('p' + name) #concatination (print('2' + '3'))
x = 'hello world'
print(x.upper()) #making whole string uppercase
print(x.split()) #spliting string into 2(splits at space)
print(x.split('l')) #spliting by passing any character
print('this is a string {}'.format('inserted')) #inserted string is cancatinated
print('the {2} {1} {0}'.format('fox','brown','quick')) #if you want to insert in any order here brown = 2, fox = 1 etc.
print('the {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#level of precision for floating point no.s
#float formatting follows "{value:width.precision f}", value is variable, width is spaces , precision is the no. of no.s after decimal point
result = 100/777
print("the result is {r:1.3f}".format(r=result))

#dot format method 
name = 'jose'
print(f'Hello, his name is {name}')
age = 3
print (f'{name} is {age} years old.') #to use multiple strings ina line
#for more printing format see https://pyformat.info/

a = '3'
convert_type = int(a)
print(f'you entered {a}')
print(type(a))
print(type(convert_type))





