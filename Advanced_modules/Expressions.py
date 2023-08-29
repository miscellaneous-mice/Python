'''
This regular expression also known as regex patterns

Primarily used to find a syntax from a text

Eg:
Take phone number normally written as (555)-555-5555
Then regex pattern for this is r"(/d/d/d)-/d/d/d-/d/d/d/d"

/d -> Specifies the pattern has digits

Using quantifiers to specify a expression in advanced format
r"(\d{3})-\d{3}-\d{4}
'''

text = "The agent's phone number is 408-555-1234. Call soon!"

print("Checking if a 'phone' is in 'text': {}".format('phone' in text))

import re

print("\nUsing regex patterns\n")
pattern = 'phone'

# Span is starting and ending location of a string
print(re.search(pattern, text))

# None means not in text
pattern = 'NOT IN TEXT'
print(re.search(pattern, text))

pattern = 'phone'
match = re.search(pattern, text)
print("Getting span of the 'phone' in 'text': {}".format(match.span()))
print("Verifying the .span() method")
print(text[match.span()[0] : match.span()[1]])
print(text[match.start() : match.end()])

print("\nNew text")
text = "my phone is a new phone"
match = re.search("phone",text) # Finds a single instance of phone in text
print("Getting span of the 'phone' in 'text': {}".format(match.span()))

print("\nGetting instance of the all 'phone' in 'text' using findall method")
matches = re.findall('phone', text) # Finds all instance of phone in text
print(matches)
print("Checking how many matches : {}".format(len(matches)))

print("\nGetting instance of the all 'phone' in 'text' using iter method")
for match in re.finditer('phone', text):
    print(match)
    print(match.group())
    print(match.span())

print("\nUsing special syntax to search using regex")

text = "My telephone number is 408-555-1234"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

print("The phone number in text {}".format(phone))
print("The phone number in text {}".format(phone.span()))

print("\n")
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print("The phone number in text {}".format(phone))
print("The phone number in text {}".format(phone.span()))

print("\n")
letter = re.search(r'\w{9}\s\w{6}', text)
print("The string in text {}".format(letter))
print("The string in text {}".format(letter.span()))

print("\n")
alphabets = re.search(r'M*', text)

print("The alphabet 'M' in text {}".format(alphabets))

print("\n")
no_count = re.search(r'\d{4}', text) 
print("Printing all number with length 4 {}".format(no_count))
no_count = re.findall(r'\d{3}', text) 
print("Printing all number with length 3 {}".format(no_count))

# Compiles 3 group of regex codes
print("\nPrinting phone number as groups")
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print("Grouped telephone number is {}".format(results.group()))
print("First batch of telephone number is {}".format(results.group(1)))
print("Second batch of telephone number is {}".format(results.group(2)))
print("Third batch of telephone number is {}".format(results.group(3)))
try:
    print("Fourth batch of telephone number is {}".format(results.group(4)))
except:
    print("No. of grouped objects exceeded")
else:
    print("Sucessful in printing grouped objects")

print("\nPrinting words as groups")
string_pattern = re.compile(r'(\w{9}) (\w{6})') 
words = re.search(string_pattern, text)
print("Grouped text is {}".format(words.group()))
print("First word is {}".format(words.group(1)))
print("Second word is {}".format(words.group(2)))

print("\n")
string_pattern = re.compile(r'\w{9} \w{6}')
words = re.search(string_pattern, text)
print("Grouped text is {}".format(words))
print("Text is {}".format(words.group()))
try:
    print("First word is {}".format(words.group(1)))
except:
    print("Can't get individual grouped objects")
else:
    print("Sucessful in printing grouped objects")


# Other Regex syntax

print("\nAdditional regex syntax")
print("\nOr operator")
print(re.search(r'cat', 'The cat is here'))
print(re.search(r'cat|dog', 'The dog is here'))

print("\nWild cards operator")
print("1) {}".format(re.findall(r'at','The cat in the hat sat there.')))
print("2) {}".format(re.findall(r'.at','The cat in the hat sat there.')))
print("3) {}".format(re.findall(r'...at','The cat in the hat went splat.')))

print("\nPower operator")
print("1) {}".format(re.findall(r'^\d', '1 is a number')))
print("2) {}".format(re.findall(r'^\d', 'The 2 is a number')))
print("3) {}".format(re.findall(r'\d$', 'number is 2')))
print("4) {}".format(re.findall(r'\d$', 'number is 2 I suppose')))
print("5) {}".format(re.findall(r'\w$', 'number is 2 I suppose')))
print("6) {}".format(re.findall(r'^\w', 'number is 2 I suppose')))

print("\nExclude operator 1")
phrase = "there are 3 numbers 34 inside 5 this sentence."
pattern = r'[^\d]' # Exclude all the digits in the phrase
print("1) {}".format(re.findall(pattern, phrase)))
print("2) {}".format(re.findall(r'[^\D]+', phrase))) # Exclude all non digits
print("3) {}".format(re.findall(r'[^\S]', phrase))) # Exclude all Non-whitespace
pattern = r'[^\d ]+' # Exclude all the digits and spaces in the phrase
print("4) {}".format(re.findall(pattern, phrase)))

print("\nExclude operator 2")
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print("1) {}".format(re.findall(r'[^!.? ]+',test_phrase))) # Exclude all punctuations in phrase
print("2) {}".format(re.findall(r'[^!.?]+',test_phrase))) 
unclean = re.findall(r'[^!.?]+',test_phrase)
clean = re.findall(r'[^!.? ]+',test_phrase)
print("3) {}".format(''.join(unclean)))
print("4) {}".format(' '.join(clean)))
# print("4) {}".format('-'.join(clean)))

print("\nAdvanced exclude operator")
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
print("1) {}".format(re.findall(r'[\w]+', text)))
print("2) {}".format(re.findall(r'[\w]', text)))
print("3) {}".format(re.findall(r'\w+-\w+', text)))
print("4) {}".format(re.findall(r'[\w]+-[\w]+', text)))
print("5) {}".format(re.findall(r'[\w]+-[\w]', text)))
text = 'Only find the hypen-words123 in this sentence 123. But you do not know how long-ish they are'
print("6) {}".format(re.findall(r'[\w\d]+', text)))
print("7) {}".format(re.findall(r'[\w\d ]+', text)))
print("8) {}".format(re.findall(r'[\w]+-[\w\d]+', text)))
print("9) {}".format(re.findall(r'\w+-\w+\d+', text)))
print("10) {}".format(re.findall(r'[\w]+-[\w]+[\d]+', text)))

print("\nParenthesis for Multiple Options")
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print("1) {}".format(re.search(r'cat(fish|nap|claw)',text)))
print("2) {}".format(re.search(r'cat(fish|nap|claw)',texttwo)))
print("3) {}".format(re.search(r'cat(fish|nap|claw)',textthree)))
print("4) {}".format(re.search(r'cat(fish|nap|erpillar)',textthree)))

'''
\S = ' '
------------------------------------------------------------------------------
.findall(pattern, text): Gives a list of elements where the element would or 
wouldn't follow the pattern given in the text.

.compile(pattern): Basically compiles the pattern for more advanced
searching methods when using .search() or other regex methods.

.search(pattern, text): Basically single element that follow the pattern given
in the text. You have more advanced features such as .span(), .group(), 
.group(n) (if pattern is used with .compile), etc.

.iter(pattern, text): Basically gives list of elements where the element follows
the pattern given in the text. You have more advanced features such as .span(),
.group(), .group(n) (if pattern is used with .compile), etc.
------------------------------------------------------------------------------
------------------------------------------------------------------------------
r'[^]' is the exclude operator

r'[^pattern(1)pattern(2)...pattern(n)]' is the exclude every pattern specified 
in the exclude operator from the text into the list. Instead include all other 
pattern such as:
pattern : r'[^\d]'
output : ['\w','\w','\w','\S','\w','\w',.......]

r'[^pattern(1)pattern(2)...pattern(n)]+' is the exclude every pattern specified
in the exclude operator from the text in the list. Instead include all other 
pattern such as:
pattern : r'[^\d]+'
output : ['\w{5}\S\w{3}','\w{3}','\S\w{4}\S',.....]
------------------------------------------------------------------------------
------------------------------------------------------------------------------
r'[]' is include operator

r'[pattern]' is the include every pattern in the text specified in the include 
operator from 
pattern : r'[\w\d]' or r'[\w][\d]'
output : ['\w','\w','\d',.....,'\w']

r'[pattern]+' is the include every pattern in the text specified in the 
include operator from 
the text into the list.
pattern : r'[\w\d]+' 
output : ['\w{3}','\w{4}','\d','\w{4}\d{2}',.....,'\w{6}']
pattern : r'[\w]+[\d]+'
output : ['\w{3}d{2}','\w{4}d{1}',.....,'\w{6}\d{3}']
------------------------------------------------------------------------------

'+' operator basically spilt text into individual segments where the elements
have been removed

Example: "there are 3 numbers 34 inside 5 this sentence."
          abcdefghijklmnopqrstuvwxyz1234567890

re.findall(r'[^\d]+', phrase)

Splits at the text at k'th, [u to v]'th, 5'th hence it will be like
['there are ', ' numbers ', ' inside ', ' this sentence.']

'''


'''
Pattern codes:

Character |	 Description     | Example Pattern Code	| Exammple Match  |
-----------------------------------------------------------------------
   \d	  | A digit	         |    file_\d\d	        |    file_25      |
   \w	  | Alphanumeric     |    \w-\w\w\w	        |    A-b_1        |
   \s	  | White space	     |    a\sb\sc	        |    a b c        | 
   \D	  | A non digit	     |    \D\D\D	        |    ABC          |  
   \W	  | Non-alphanumeric |	  \W\W\W\W\W	    |    *-+=)        |
   \S	  | Non-whitespace   |	  \S\S\S\S	        |    Yoyo         |  


Character |	 Description             | Example Pattern Code	| Exammple Match  |
-------------------------------------------------------------------------------
   +	  | Occurs one or more times |    Version \w-\w+    |  Version A-b1_1 |
  {3}	  | Occurs exactly 3 times   |    \D{3}	            |  abc            |
  {2,4}   | Occurs 2 to 4 times      |    \d{2,4}           |  123            | 
  {3,}	  | Occurs 3 or more         |    \w{3,}            |  anycharacters  |  
  \*	  | Occurs zero or more time |	  A\*B\*C*	        |  AAACC          |
  ?	      | Once or none             |	  plurals?          |  plural         |  
'''