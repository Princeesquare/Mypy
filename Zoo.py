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
    pass


class Hawk(animals):
    pass


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.sleep()
hawk.eat()
