
print('Python program to display all the prime numbers within an interval')

lower = 0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


print('\n')
print('write a function that takes a list of integers and returns true if the number contains 007')
def spy_games(nums):
    code = [0,0,7,'x']
    #[0,7,'x']
    #[7,'x']
    #['x'] length of the array = 1
    for num in nums:
        if num == code[0]:
            code.pop(0) 
    return len(code) == 1 

print(spy_games([1,2,4,0,0,7,5]))

print('\n')
print('write a function that returns the number of prime numbers that exist upto and including the given number')
def count_prime(num):
    #check for input 0 or 1
    if num < 2:
        return 0

    #2 or greater 

    #store our prime numbers
    primes  = [2]
    x = 3
    while x <=num :
        for y in range(3,x,2):  #starts from 3 ends at x and increments loop in step size of 2 as even are not prime numbers
            if (x%y)==0: 
                x += 2
                break
        else:                    #if for loop never broke we are going to add that number to our prime list
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)
count_prime(100)







