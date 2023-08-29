def add(a,b):
    return a + b

num1 = 10
#num2 = input("enter the other number to add: ")  #to add error
# num2 = 'a'  #to add error
num2 = 20

try:
    result = add(num1, num2)
except TypeError:
    print("looks like you arent adding numbers properly i.e. type error")
except:
    print("all other exceptions")
else:
    print("Above program went well")
    print(result)


try:
    f = open('testfile_1','w')  #change it r to w
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()


try:
    f = open('testfile_2','r')
    f.write('Test write this')
except:
    # This will check for any exception and then execute this print statement
    print("Error: Could not find file or read data")
else:
    print("Content written successfully")
    f.close()


try:
    f = open("testfile_3", "r")
    f.write("Test write statement")
    f.close()
except OSError:
    print('You have an OSError')
except:
    print('all other exceptions')
finally:
    print("Always execute finally code blocks")


def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        finally:
            print("Finally, I executed!")

askint()