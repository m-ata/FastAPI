
# Method Overriding (Class Inheritance)

class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Animal(),Dog(), Cat()]

for animal in animals:
    print(animal.speak())  # Output: Bark! and Meow!



# Duck Typing (Python-specific)

class Bird:
    def fly(self):
        print("Flying in the sky!")

class Airplane:
    def fly(self):
        print("Flying with jet engines!")

def lift_off(flying_object):
    flying_object.fly()

# Polymorphism in action
lift_off(Bird())       # Output: Flying in the sky!
lift_off(Airplane())   # Output: Flying with jet engines!
