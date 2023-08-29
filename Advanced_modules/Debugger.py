x = [1 ,2 ,3]
y = 2
z = 3

result = y+z
print("Result of y+z is {}".format(result)) # But this gets printed before error
try:
    result2 = x+y # Hence we know Error is on this line
except:
    print("There is an error")
else:
    print("Result of x+z is {}".format(result2))

import pdb # Python Debugger

print("\nUsing python Debugger")

x = [1 ,2 ,3]
y = 2
z = 3

# Set trace before the error line
print("You can do write: x\ny\nx+y\nz\nz+y\nAnd 'q' to come out")
pdb.set_trace()

