class Book:
    def __init__(self, author, year):
     self.author = author
     self.year = year
    
    def myfunc(self):
        print("The book was written by " + self.author)

b1 = Book("Wellington", 2009)
b1.myfunc()


# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass 1: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass 2: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass 3: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Call move() on each
my_car.move()     
my_plane.move()   
my_boat.move()    
