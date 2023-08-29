class Sample:
    pass

# Instance of Sample
x = Sample()

print(type(x))

#different types of attribute assignments
print('\n')
class Dog:
    def __init__(self,breed):
        self.breed = breed     # 1) self.breed = mybreed 2) pass def __init__(self,mybreed):  3) sam = Dog(mybreed='lab') 
                               # in print function it's the same i.e sam.breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
print(sam.breed)
print(frank.breed)

#multiple attributes
print('\n')
class Dog:
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self, number):      #to call use method
        print("woof my name is {} and the number is {}".format(self.name, number))    
my_dog = Dog('Lab','Sam')
print(my_dog.name)
print(my_dog.species)  #can be used with sam too its not connected to one class

my_dog.bark(10)  #to use methods use parenthesis

print("\n")

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):  #you can have default radius value or you can set it by calling c = Circle(30) etc
        self.radius = radius 
        self.area = radius * radius * Circle.pi   #you can even call it as self.pi but as pi is a class attribute you can use circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = self.radius * self.radius * self.pi  #self.pi as its different instance and not user input

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

c.setRadius(10) # can change the radius here

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())

print("inheritance \n")

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Food")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)   #it creates the init instance from the class Animal
        print("Dog created")

    def Hi(self):
        print("Dog")

    def bark(self):
        print("Woof!")

    def whoAmI(self):
        print("updated to dog")


d = Dog()    #now you can use all the features of animal class in dog as its inherited for eg , if 86 to 90 line were commented 
             #you could still use d.whoAmI() and it would take method from the class Animal
d.whoAmI()

d.Hi()

d.eat()

d.bark()

print("\n polymorphism \n")  # https://www.geeksforgeeks.org/polymorphism-in-python/

class Tiger:
    def __init__(self, name):
        self.name = name
        print("tiger is named {}".format(name))

    def speak(self):
        return self.name+' says roar!'
    
class Cat:
    def __init__(self, name):
        self.name = name
        print("cat is named {}".format(name))

    def speak(self):
        return self.name+' says Meow!' 
    
niko = Tiger('Niko')
felix = Cat('Felix')

print("\nprint method")
print(niko.speak())
print(felix.speak())

print("\nforloop method")
for pet in [niko,felix]:     #instead of line 126 and 127
    print(pet.speak())

print("\nfunction method")
def pet_speak(pet):         #in function format
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

print("\n example 2\n")
class Species:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cow(Species):  
    def speak(self):          #no need of _init_ as its inherited an Animal class will take care of that
        return self.name+' says MOO!'
    
class Crow(Species):
    def speak(self):
        return self.name+' says Kaww!'
    
fido = Cow('Fido')
isis = Crow('Isis')

print(fido.speak())
print(isis.speak())


print("\n special OOPS methods \n")
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):   #you can now print the Books by just printing unlike the erroe you got
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages) 

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)  #about book
print(len(book))  #number of pages
# del book  #delete the book from your computers memory
#print(book) ->  Error 

print("\n")
print("homework for oops")

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

c1 = (2, 5)
c2 = (4, 1)
line = Line(c1, c2)
print(line.distance())

print("\n")
print("homework 2")
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.height * 3.14 * self.radius ** 2
    
    def surface_area(self):
        top = 3.14 * self.radius ** 2
        return (2*top) + (2*3.14*self.radius*self.height)


cylinder = Cylinder(5, 2)
print(cylinder.volume())

print("\n")
print("Chanllenge")
class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        print(f'the balance is : ${self.balance}')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
            print(f'the balance is : ${self.balance}')
        else:
            print('Funds Unavailable!')
# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)
acct1.deposit(20)
acct1.withdraw(119)




