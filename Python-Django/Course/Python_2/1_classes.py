# CLASSES

###################
# Attributes
###################
class Dog():
  # Class Object attribute: same for all class instances
  # defined outside of any methods
  species = "mammal"

  # Special method called when object is created
  # initializes attributes of object instance (self)
  def __init__(self,breed,name):
    # Class instance attribute
    self.breed = breed
    self.name = name

mydog = Dog("Lab","Sammy")
print(mydog) # <__main__.Dog object at 0x10335bd08>
print(mydog.species) # mammal
print(mydog.breed) # Lab
print(mydog.name) # Sammy

###################
# Methods
###################

class Circle():
  pi = 3.14

  # instantiate with radius (default=1)
  def __init__(self, radius=1):
    self.radius = radius

  # Method to calculate area
  # self.radius used for instance's radius
  def area(self):
    return self.radius * self.radius * Circle.pi

  # Method to set radius
  def set_radius(self, new_radius):
    self.radius = new_radius

  # Method to get radius (Same as calling .radius)
  def get_radius(self):
    return self.radius

myc = Circle(3)
print(myc.radius) # 3
print(myc.area()) # 28.26
myc.set_radius(10)
print(myc.get_radius()) # 10
print(myc.area()) # 314.0
print()

###################
# Inheritance
###################

class Animal():
  def __init__(self):
    print("Animal created")
  def whoAmI(self):
    print("Animal")
  def eat(self):
    print("Eating")

mya = Animal() # Animal created
mya.whoAmI() # Animal
mya.eat() # Eating

class Cat(Animal):
  def __init__(self):
    Animal.__init__(self)
    print("Cat created")
  def sound(self):
    print("MEOW")

mycat = Cat() # Cat created
mycat.whoAmI() # Animal
mycat.eat() # Eating
mycat.sound() # MEOW
print()

###################
# Special Methods
###################

class Book():
  def __init__(self, title, author, pages):
    print("A book is created")
    self.title = title
    self.author = author
    self.pages = pages
  
  # special methods allow Python specific functions on objs
  def __str__(self):
    return "Title: %s, author: %s, pages: %s " %(self.title, self.author, self.pages)
  def __len__(self):
    return self.pages
  def __del__(self):
    print("A book is destroyed")

b = Book("Python", "jose", 200) # A book is created
print(b) # Title: Python, author: jose, pages: 200 
print(len(b)) # 200
del b

