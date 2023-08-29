# grabbing word starting with s 
st = 'Sam  Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)
    
#write a program to that prints the integers from 1 to 100. but for multiples of three print 'fizz' for multiples of five print 'buzz' 
#and for multiples of both 3 and 5 print 'fizzbuzz'
for num in range(1,101):
    if num%3 == 0 and num%5 ==0:
        print('fizzbuzz')
    elif num%3 == 0:
        print('fizz')
    elif num%5 == 0:
        print('buzz')
    else:
        print(num)


#first letter of every word from above string 
print([word[0] for word in st.split()])

print('\n')
print('to print alternate numbers as uppercase')
def myfunc(test_str = 'whoareyou'):
    res = ""
    for idx in range(len(test_str)):
        if not idx % 2 :
            res = res + test_str[idx].upper()
        else:
            res = res + test_str[idx].lower()
    return res

string = myfunc("geeks")
print(string)

print('\n')
print('prime numbers')
def primenum(a):
    lower = 0
    upper = a
    n = 0
    for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                n = n+1
    return n


print(primenum(100))

print('\n')
print('write a function that takes two word string and returns true if both string start with same word')
def animal_cracker(text):
    wordlist = text.lower().split()  #split by lower casing after splitting

    return wordlist[0][0] == wordlist[1][0]

print(animal_cracker('levelhead Llama'))

print('\n')
print('write a fuction to capitalize first and fourth letters of the word')
def old_mcdonald(name):
    letter_one =  name[0]
    middle_letter = name[1:3]
    fourth_letter = name[3]
    rest =  name[4:]
    return letter_one.upper() + middle_letter + fourth_letter.upper() + rest
print(old_mcdonald('oldmcdonald'))

print('\n')
print('reverse the sentence')
def master_yoda(text):
    wordlist = text.split() 
    reverse_wordlist = wordlist[::-1]
    return ' '.join(reverse_wordlist)  #line1 mylist = ['a', 'b', 'c'] line2 '--'.join(mylist) output a--b--c

print(master_yoda('i am home'))

print('\n')
print('subraction and if the number is within 10 from 100 or 200')
def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n)<= 10)

print(almost_there(90))

print('\n')
print('if 3 repeats together')
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False  

print(has_33([1,3,5,3,4]))  

print('\n')
print('print every charcater in word 3 times')
def paper_doll(text):
    result = ''

    for char in text:
        result += char*3  #result += char + char + char
    return result

print(paper_doll('hello'))

print('\n')
print('Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9')
def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,2,6,8,9,11]))

print('\n')
print('to check whether a number is in the given range')
def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')
# Check
ran_check(5,2,7)

# for the above code we could also use :  return num in range(low, high+1)

print('\n')
print('to get unique value from the array')
def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

#solution to this problem is in lecture 58 18:10
print('\n')
print('Write a Python function to check whether a string is pangram or not.')
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  
print(ispangram("The quick brown fox jumps over the lazy dog"))
string.ascii_lowercase

