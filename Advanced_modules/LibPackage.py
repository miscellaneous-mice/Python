class PythonLib:
    
    #@classmethod
    
    def lib_ref(self, lib):

        #default = "incorrect library"
                
        print("\nIt's a Library\n")
        
        #return getattr(self, lib.upper(), lambda: default)()
                
        return getattr(self, lib.upper(), None)()
 

    def COLLECTIONS(self):
        
        print("this library is :",'\033[1m' + 'Collections\n' + '\033[0m' )

        import Collections

        print("\nThats it in collections module")
    
    def OSMODULE(self):

        print("this library is :",'\033[1m' + 'OS module\n' + '\033[0m' )

        import OS_module

        print("\nThat's it in OS module")

    def DATETIME(self):

        print("this library is :",'\033[1m' + 'datetime module\n' + '\033[0m' )

        import DateTime

        print("\nThat's it in datetime module")
    
    def MATH(self):

        print("this library is :",'\033[1m' + 'Math and Random module\n' + '\033[0m' )

        import Math_random

        print("\nThat's it in Math and Random module")

    def DEBUGGER(self):

        print("this library is :",'\033[1m' + 'Debugger module\n' + '\033[0m' )

        import Debugger

        print("\nThat's it in Debugger module")

    def EXPRESSIONS(self):

        print("this library is :",'\033[1m' + 'regex module\n' + '\033[0m' )

        import Expressions

        print("\nThat's it in regex module")
    
    def TIMING(self):

        print("this library is :",'\033[1m' + 'timit module\n' + '\033[0m' )

        import Timing

        print("\nThat's it in timit module module")   

    def ZIPPING(self):

        print("this library is :",'\033[1m' + 'Zip/Unzip module\n' + '\033[0m' )

        import Zipping

        print("\nThat's it in Zip/Unzip module module")    
 
