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
# Multi-level Inheritance: family tree of grandparents, parents and child

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

# Multiple Inheritance: a child class is derived from more than one parent class

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


# Method Override

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

# Method chaining: is used to call multiple method sequentially
# each call performs an action on the same object

class car:
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


my_car = car()

my_car.turn_on().drive()
my_car.brake().turn_off()
my_car.turn_on() \
    .drive() \
    .brake() \
    .turn_off()  # Method chaining

