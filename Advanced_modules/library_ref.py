from LibPackage import PythonLib
import inspect
import difflib

# The below function checks if the libraries contain the user's input
def has_method(o, name):  
    return callable(getattr(o, name, None))

# Removes the all spaces from the input
def remove(string):

    return string.replace(" ", "")

# Checks which is the closest matching library or operation w.r.t the users input
def strn(str1, str2):

    similarity = difflib.SequenceMatcher(None, str1, str2).ratio()

    str_op =  similarity*100
    return str_op

# Basically returns definition to Library with matches with the users input
def expected(d):
  return max(d, key = d.get)

#Go = "test"
max_dict = {}
my_library = PythonLib()

bool_var = True

Libraries = inspect.getmembers(PythonLib, predicate=inspect.isfunction)

print(f"\nLibraries are\n")

enum = 0

for libs in Libraries:
    if (libs[0] == 'lib_ref'):
        break
    else:
        enum = enum + 1 
        print(f"{enum}) {libs[0]}\n")

while(bool_var):
    
    choose = input("\nLibrary you wanna access : ")
    choose = choose.upper()
    
    Go = remove(choose)

    for Lib,address in Libraries:
        similar = strn(Lib, Go)
        max_dict[Lib] = similar

    Go = expected(max_dict)

    while(True):

        yes_no = input("\nDid you mean '{}'. Type 'y' for Yes and 'n' for NO: ".format(Go))
        yes_no = yes_no.lower()

        if(yes_no == 'y'):

            if(has_method(my_library, Go.upper())):

                bool_var = False

                my_library.lib_ref(Go)

                break
                
            else:
                
                print("\nLibrary not found!! Try again :)")

                bool_var = True

                break

        elif(yes_no == 'n'):

            print("Choose the library again")

            bool_var = True

            break

        else:
            print("Couldn't Interpret the Answer as Yes or no!. Try Again")
            continue

        