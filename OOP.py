# CLASS VARIABLES
class Car:
    wheels = 4  # Class variables: attributes that is common to all instances in the class

    # Class variable's value can be accessed by all instances in the class

    def __init__(self, make, model, year, color):  # __init__ is a constructor that holds common attributes of a class
        self.make = make  # instance variable is declared inside a constructor and assigned unique values
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")


# INHERITANCE


class animals:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(animals):  # Rabbit is the child class while the parameter "animal" is the parent class
    def run(self):  # Rabbit will inherit all the attributes of the parent class.
        print("This rabbit is running")


class Fish(animals):
    def swim(self):
        print("This fish is swimming")


class Hawk(animals):
    def fly(self):
        print("This hawk is flying")


def test1():
    rabbit = Rabbit()
    fish = Fish()
    hawk = Hawk()

    print(rabbit.alive)
    fish.sleep()
    hawk.eat()

    rabbit.run()
    fish.swim()
    hawk.fly()


# test1()

# MULTI-LEVEL INHERITANCE: family tree of grandparents, parents and child

class Organism:
    alive = True


class Animal(Organism):

    def eats(self):
        print("This animal is eating")


class Dog(Animal):
    def bark(self):
        print("This dog is barking")


def test2():
    dog = Dog()
    print(dog.alive)
    dog.eats()
    dog.bark()


# test2()


# MULTIPLE INHERITANCE: a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


def test3():
    rabbit = Rabbit()
    hawk = Hawk()
    fish = Fish()

    rabbit.flee()
    hawk.hunt()
    fish.flee()
    fish.hunt()


# test3()


# METHOD OVERRIDE

class Animal:
    def eats(self):
        print("This animal is eating")


class Rabbit(Animal):

    def eats(self):
        print("This rabbit is eating a carrot")


def test4():
    rabbit = Rabbit()
    rabbit.eats()


# test4()

# METHOD CHAINING: is used to call multiple method sequentially
# each call performs an action on the same object
# for method chaining to work, the method has ro return self after the statements

class Benz:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You stopped the car")
        return self

    def turn_off(self):
        print("You turned off the engine")
        return self


def test5():
    my_car = Benz()
    my_car.turn_on().drive()
    my_car.brake().turn_off()
    my_car.turn_on() \
        .drive() \
        .brake() \
        .turn_off()  # Method chaining


# test5()


# Super() = Function used to give access to the methods of a parent class
# It returns a temporary object of a parent class when used


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


def test6():
    square = Square(3, 3)
    cube = Cube(3, 3, 3)

    print(square.area())
    print(cube.volume())


# test6()


#  ABSTRACT CLASSES: this prevents a user from creating an object of that class
# it compels a user to override abstract methods in a child class

# abstract class is a class which contains one or more abstract methods
# abstract method is a method that has a declaration but does not have an impementation

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Cars(Vehicle):
    def go(self):
        print("You are driving the car")

    def stop(self):
        print("Stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You are riding the motorcycle")

    def stop(self):
        print("Stop the Motorcycle")


def test7():
    # vehicle = Vehicle()
    car = Cars()
    bike = Motorcycle()

    # vehicle.go()
    car.go()
    car.stop()
    bike.go()
    bike.stop()


# test7()


# PASSING OBJECTS AS ARGUMENTS

class Motor:
    color = None


class Bikes:
    color = None


def change_color(car, color):
    car.color = color


def test8():
    car1 = Motor()
    car2 = Motor()
    car3 = Motor()
    biker = Bikes()

    change_color(car1, "Blue")
    change_color(car2, "Grey")
    change_color(car3, "Black")
    change_color(biker, "Purple")

    print(car1.color)
    print(car2.color)
    print(car3.color)
    print(biker.color)


# test8()


# DUCK TYPING
# This is a concept where the class of an object is less important than the methods/attributes
# class type is not checked if minimum methods/attributes are present


class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")


def test9():
    duck = Duck()
    chicken = Chicken()
    person = Person()
    person.catch(duck)

# test9()
