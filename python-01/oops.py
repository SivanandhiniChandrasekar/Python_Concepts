# OOPS -  To make the real world object properties in computer using programming language.
# Class, object, abstraction, encapsulation, polymorphism, inheritance.
# Class - Its a blueprint to create object.
# object - It is an instance of the class.
# Difference between Object oriented programming and Strucutred language.

# Calculator - 
# sum - 2 parmeter, 3 parameter, arr
# subtraction - 2 para

class Animal:
    def habitat(self):
        print("Animal Lives in Forests")
        

class Dog(Animal):
    def habitat(self):
        print("Dog lives in Home or Street as well!")

class Cat(Animal):
    def habitat(self):
        print("Cat also lives in home or forests!")


# dog = Dog("Tommy")
# cat = Cat("Minion")
dog = Dog()
dog2 = Dog()
cat = Cat()

dog.habitat()
cat.habitat()

