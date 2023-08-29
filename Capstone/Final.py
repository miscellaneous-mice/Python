from __future__ import print_function
import math, sys
from decimal import * # import all attributes of a module
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

def factorial(n):
	"""
	Return the Factorial of a number using recursion

	Parameters:
	n -- Number to get factorial of
	"""
	if not n:
		return 1
	return n*factorial(n-1)


def getIteratedValue(k):
	"""
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.. Since we need k decimal places
	make iterations equal to k+1
	
	Parameters:
	k  -- Number of Decimal Digits to get
	"""
	k = k+1
	getcontext().prec = k
	sum=0
	for k in range(k):
		first = factorial(6*k)*(13591409+545140134*k)
		down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
		sum += first/down 
	return Decimal(sum) 

def getValueOfPi(k):
	"""
	Returns the calculated value of Pi using the iterated value of the loop
	and some division as given in the Chudnovsky Algorithm

	Parameters:
	k -- Number of Decimal Digits upto which the value of Pi should be calculated
	"""
	iter = getIteratedValue(k)
	up = 426880*math.sqrt(10005)
	pi = Decimal(up)/iter 
	
	return pi

def shell():
	"""
	Console Function to create the interactive Shell.
	Runs only when __name__ == __main__ that is when the script is being called directly

	No return value and Parameters
	"""
	print ("Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

	while True:
		print (">>> ", end='')
		entry = input()
		if entry == "quit":
			break
		if not entry.isdigit():
			print ("You did not enter a number. Try again")
		else:
			print (getValueOfPi(int(entry)))

if __name__=='__main__':
	shell()