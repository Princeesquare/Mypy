class Car:

    wheels = 4  # Class variables: attributes that is common to all instances in the class
                # Class variable's value can be accessed by all instances in the class

    def __init__(self, make, model, year, color):  # __init__ is a constructor that holds common attributes of a class
        self.make = make   # instance variable is declared inside a constructor and assigned unique values
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")
