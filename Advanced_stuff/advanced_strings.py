s = 'hello world'

print("captialize : {}".format(s.capitalize()))

print("uppercase : {}".format(s.upper()))

print("lowercase : {}".format(s.lower()))

print("count o : {}".format(s.count('o')))

print("location of o : {}".format(s.find('o')))

print("Center : {}".format(s.center(20, 'z'))) # 20 -> length of resulting string

print("Hello\tHi")

print("Hello\tHi".expandtabs())

s = 'hello'

print("Checking if it is alphanum : {}".format(s.isalnum()))

print("Checking if it is alpha : {}".format(s.isalpha()))

print("Checking if it is lowercase : {}".format(s.islower()))

print("Checking if it is space : {}".format(s.isspace()))

print("Checking if it is Titled : {}".format(s.istitle())) # 'H'ello

print("Checking if it is uppercase : {}".format(s.isupper())) # HELLO

print("Checking if it is uppercase : {}".format(s.endswith('o'))) # s[-1] == 'o'

print("\nAdvanced Regex Operations")

print("1 : {}".format(s.split('e')))

s = 'hiiihihhihiihhhi'

print("2 : {}".format(s.split('i')))

print("3 : {}".format(s.partition('i')))