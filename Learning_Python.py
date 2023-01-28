def variables():
    # This function explains how to assign variables
    fname = "Emmanuel"  # This is a string variable by default
    sname = "Ezenwa"
    full_name = fname + sname
    age = 3  # This is an integer variable
    print(type(full_name), type(age))  # This commandline prints the variable types


# variables()


def mathop():
    # This function explains how to use mathematical operators
    x = 1
    y = 2.1
    z = "3"

    x = str(x)
    y = int(y)
    z = int(z)

    print("X is equal to " + x)
    print(y)
    print(z * 3)


# mathop()


def userinput():
    # This functions shows how to collect information from a user
    name = input("What is your name?: ")  # The f
    age = int(input("How old are you: "))
    height = float(input("How tall are you: "))

    age += 1

    print("Hello " + name)
    print("You're gonna be " + str(age) + " Years old by next year.")
    print("You are " + str(height) + "cm tall")


# userinput()


import math


# This is used to import mathematical functions such as power, round off e.t.c
# To use math module, "import math must be included in the program


def mathlib():
    # This function shows the usage of math module
    pi = 3.14

    x = 2
    y = 8
    z = 4

    print(round(pi))
    print(abs(pi))
    print(math.ceil(pi))
    print(math.floor(pi))
    print(pow(pi, 2))
    print(math.sqrt(pi))
    print(max(x, y, z))
    print(min(x, y, z))


# mathlib()


def string_slicing():
    # String slicing using indexing [start:stop:step] or slice(start,stop) method

    name = "Emmanuel Ezenwa"
    first_name = name[0:4]
    last_name = name[9:]
    mid_name = name[::2]
    backwards = name[::-1]

    print(first_name)
    print(last_name)
    print(mid_name)
    print(backwards)
    print(last_name)

    website = "http://google.com"
    web = "http://sis.ciu.edu.tr.com"
    slicing = slice(7, -4)

    print(website[slicing])
    print(web[slicing])


# string_slicing()


def if_elif_conditionals():
    # if statements (elif stands for else if)

    age = int(input("How old are you?: "))

    if 18 <= age <= 99:
        print("You are an adult!")
    elif age == 100:
        print("You are a century old!!")
    elif age < 0:
        print("You are yet to be born!! Go back to the womb lol!!")
    else:
        print("You are a child!")


# if_elif_conditionals()


def logicalops():
    # Logical Ops (and, or and not)

    temp = int(input("What is the temperature outside?: "))

    if temp >= 0 and temp <= 30:  # 0 <= temp <= 30 is a simpler way to write it
        print("The weather is good today so you can go outside.")
    elif temp < 0 or temp > 30:
        print("The weather is not friendly, please stay inside!!")
    elif not 100 < temp < -50:
        print("The weather is not too good but you can go out and be cautious")


# logicalOps()


def while_loop():
    # While loop is unlimited depending on the condition

    name = ""

    while name == "":
        name = input("Please Enter your name: ")

    print("Hello " + name)


# while_loop()


def for_loop():
    # for loop has a limit because we know the end

    for i in range(10, 101, 2):
        print(i)

    for i in "Ezenwa Emmanuel":
        print(i)


# for_loop()


import time


# This commandline adds time to the program to add delay


def timedelay():
    # This functions shows how to use the time module to add delay to a program

    for secs in range(10, 0, -1):
        print(secs)
        time.sleep(2)
    print("Happy New Year!!!")


# timedelay()


def nested_loop():
    # Nested loops is basically loop in a loop

    rows = int(input("How many rows: "))
    cols = int(input("How many columns: "))
    sym = input("Enter a symbol: ")

    for i in range(rows):  # row loop
        for j in range(cols):  # loop in-charge of columns
            print(sym, end="")
        print()


# nested_loop()


def loop_control():
    # Loop Control Statements (break//terminates the loop,
    # continue keyword skips the next iteration
    # pass acts as a placeholder)

    while True:
        name = input("Enter your name: ")
        if name != "":
            print("Thank you!!")
            break

    phno = "123-456-789"

    for i in phno:
        if i == "-":
            continue
        print(i, end="")

    for i in range(1, 21):
        if i == 13:
            pass
        else:
            print(i)


# loop_control()


def lists():
    # List is a collection that stores multiple items in a single variable

    food = ["Pizza", "Beans", "Burger"]

    food.append("rice")  # Adds a new element to the end of the list
    food.remove("Pizza")  # Removes a specified item
    food.pop()  # Removes the element at the end of the list
    food.insert(0, "Pudding")

    for i in food:
        print(i, " ", end="")


# lists()


def twoD_lists():
    # 2D lists = a list of list

    drinks = ["coffee", "tea", "cola"]
    meal = ["spaghetti", "rice", "pudding"]
    dessert = ["cake", "cookies", "chocolate"]

    dinner = [drinks, meal, dessert]

    print(dinner)
    print(dinner[1][2])


# twoD_lists()


def tuples():
    # Tuples (Ordered and unchangeable)

    student = ("Emm", 21, "male")

    print(student.index("male"))
    print(student.count("Emma"))

    for x in student:
        print(x)
    if "Emma" in student:
        print("Yes Emma is present in student")
    else:
        print("There's no word as such in student")


# tuples()


def sets():
    # SET (Unordered and no duplicates)

    utensils = {"fork", "knife", "spoon", "pot"}

    utensils.add("pan")
    utensils.remove("knife")

    dishes = {"Cup", "bowl", "pot", "fork"}
    utensils.update(dishes)
    utensils.add("kettle")

    dinner_table = utensils.union(dishes)
    dinner_table = utensils.symmetric_difference(dishes)

    dinner_table = utensils.difference(dishes)
    dinner_table = utensils.intersection(dishes)

    for i in dinner_table:
        print(i)


# sets()


def dictionaries():
    # Dictionaries (Changeable, Unordered and Unique key:value pair)

    capitals = {"USA": "Washington DC",
                "Nigeria": "Abuja",
                "Russia": "Moscow",
                "China": "Beijing"}

    # get keyword is used to check if there is a key in the dict without returning an error if it's not available
    print(capitals.get("China"))

    print(capitals.items())

    for key, value in capitals.items():
        print(key, value)

    capitals.update({"Germany": "Berlin"})
    capitals.update({"USA": "Texas"})
    print(capitals)
    capitals.pop("USA")
    capitals.clear()
    # del capitals
    print(capitals)


# dictionaries()


def indexing():
    # indexing [] = gives access to sequence's element (str, lists, tuples)

    name = "Emmanuel Ezenwa"

    if name[0].islower():
        name = name.capitalize()
        print(name)
    else:
        print("Name at index 0 is already capitalized")

    nickname = name[:4].upper()
    surname = name[8:]
    print(nickname, surname)


# indexing()


def task1():
    # Taking birth year from 2 users and comparing the age
    a = int(input("What year where you born: "))
    b = int(input("Please enter your birth year: "))

    c = 2022 - a
    d = 2022 - b

    if c == d:
        print("\nThe ages are the same!")
        print("\nThe age of the first is: ", c, "\nThe age of the second is:", d)
    else:
        print("\nThe ages are not the same!")
        print("\nThe age of the first is: ", c, "\n\nThe age of the second is:", d)


# task1()


def task2():
    # Taking unknowns from a user to calculate a formula f
    x = float(input("Please Enter a value for x: "))
    y = float(input("Please Enter a value for y: "))
    z = float(input("Please Enter a value for z: "))

    exp1 = 3 * pow(x, 2) + (4 * z * x) + y
    exp2 = (z * y) + x

    f = round(y * (exp1 / exp2), 2)
    print("The result of the equation f = ", f)


# task2()


def task3():
    # Sum of even numbers within a range of numbers
    add = 0

    for x in range(1, 11):
        if x % 2 == 0:
            add += x
            print(x)


# task3()


def task4():
    # Display a menu and perform an operation based on the selected option
    print("1. Calculate Multiplication"
          "\n2. Calculate Addition"
          "\n3.Calculate Subtraction"
          "\n4. Calculate Division")

    choice = int(input("\nOption: "))

    a = int(input("\nEnter value one: "))
    b = int(input("\nEnter value two: "))

    match choice:
        case 1:
            c = a * b
            print("The result is: ", c)

        case 2:
            c = a + b
            print("The result is: ", c)
        case 3:
            c = a - b
            print("The result is: ", c)
        case 4:
            c = float(a / b)
            print("The result is: ", c)
        case 5:
            print("\nPlease Enter a valid Option!!!")


# task4()


def function():
    # Function is a block of code that executes only when it's called.
    # Function starts with the keyword "def" to define the function
    # A function takes parameters , while the function call takes arguments.
    # using keyword arguments
    # Keyword argument are arguments preceded by an identifier when passing them to a function
    # In positional argument, the order of arrangement matters, but arrangement doesn't matter in keyword argument.
    pass


def hello(fname, sname):
    print(fname, " ", sname)


def kwarg_eg():
    name = input("Enter First name: ")
    surname = input("Enter Surname: ")
    hello(sname=name, fname=surname)  # Example of keyword arguments


# kwarg_eg()

# Return statements in python is used to send values/objects back to the caller

def mul(num1, num2):  # num1 and num2 are parameters
    return num1 * num2


def task5():
    # Taking input from a user and passing it as an argument to a function
    a = int(input("Enter a first number: "))
    b = int(input("Enter a second number: "))
    c = mul(a, b)
    # a, b are positional arguments. the value is passed to num1 by default while the value of b is passed into num2
    # The result of the function is returned and stored in the variable c
    print("The result of your number after multiplying is: ", c)


# task5()


def nested_function_calls():
    # Nested function call is a function call inside another function call
    print(round(abs(float(input("Enter a whole positive number: ")))))


# nested_function_calls()


def args():
    # args is short for arguments
    # args is a parameter that will pack all arguments into a tuple[]
    # It is useful so a function can accept a varying number of arguments
    # using args as a parameter will allow the function call take an unlimited number of arguments in the function call
    # to use args as a parameter, it must be preceded by an asteriks(*)
    # after the asteriks, (*) any name can be used as an args
    pass


def addition(*args):
    # This function will show how to use args as a parameter
    sumof = 0
    for i in args:
        sumof += i
    return sumof


def args_test():
    c = addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    # The addition function takes an unlimited number of arguments
    print("The sum of values in addition is:", c)


# args_test()


def kwargs():
    # kwargs is short for keyword arguments
    # kwargs is a parameter that will pack all arguments into a dictionary
    # It is useful so a function can accept a varying number of arguments
    # using kwargs as a parameter will allow the function call take an unlimited number of arguments when called
    # to use kwargs as a parameter, it must be preceded by two asteriks(**)
    # after the asteriks, (*) any name can be used as an args
    pass


def names(**kwarg):
    print("\nHello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


def kwargs_test():
    fname = input("Enter first name: ")
    mname = input("Enter middle name: ")
    sname = input("Enter last name: ")
    names(first=fname, middle_name=mname, last_name=sname)


# kwargs_test()


def string_format():
    # Format is a string method that gives users more control when displaying output
    # The curly braces are known as format fields that act as a placeholder
    # The curly braces can take arguments inform of index or variable
    # The arguments can either be positional or keywords from the format method

    animal = "cow"
    item = "moon"

    print("The {} jumped over the {}".format(animal, item))
    print("The {0} jumped over the {1}".format(animal, item))  # Positional arguments
    print("The {animal} jumped over the {item}".format(animal="sheep", item="fence"))  # Kwargs
    # print("The",animal,"jumped over the",moon") is an alternative way without format method
    # formatting a string variable

    text = "The {} jumped over the {}"
    print(text.format(animal, item))
    # Adding Paddings to the format display
    print("The {:<10} jumped over the {}".format(animal, item))  # left indentation of format field (default)
    print("The {:>10} jumped over the {}".format(animal, item))  # right indentation of format field
    print("The {:^10} jumped over the {}".format(animal, item))  # centre indentation of format field
    print("The {1:^10} jumped over the {0:^10} at night".format(animal, item))
    # indentation with values or variables in field

    # Formatting numbers

    pi = 3.14159
    print("\nThe number pi is {:2f}".format(pi))
    number = 1000000
    print("The number pi is {:,}".format(number))  # adding (,) to thousands in numbers
    print("The number pi is {:b}".format(number))  # converting a number to binary format
    print("The number pi is {:o}".format(number))  # converting a number to octa-decimal
    print("The number pi is {:X}".format(number))  # converting a number to hexadecimal
    print("The number pi is {:e}".format(number))  # converting a number to a decimal notation


# string_format()


# Random numbers
import random


def random_numbers():
    # Random module is used to generate random number within a range
    # To use random, add "import random" module to your program

    x = random.randint(1, 10)  # This line will print random values between 1-10
    y = random.random()  # This line will print random float numbers between 0-1
    print(x)
    print(y)


# random_numbers()


def rock_paper_scissors():
    while True:
        my_list = ['rock', 'paper', 'scissors']
        comp = random.choice(my_list)  # This line prints random string from the list
        # print(comp)
        player = " "
        while player not in my_list:
            print("Select either rock, paper or scissors")
            player = input("rock, paper, or scissors?: ").lower()
        if player == comp:
            print("Comp: ", comp)
            print("You: ", player)
            print("It's a TIE")
        elif player == "rock":
            if comp == "paper":
                print("Comp: ", comp)
                print("You: ", player)
                print("You LOSE")
            if comp == "scissors":
                print("Comp: ", comp)
                print("You: ", player)
                print("You WIN")
        elif player == "scissors":
            if comp == "rock":
                print("Comp: ", comp)
                print("You: ", player)
                print("You LOSE")
            if comp == "paper":
                print("Comp: ", comp)
                print("You: ", player)
                print("You WIN")
        elif player == "paper":
            if comp == "scissors":
                print("Comp: ", comp)
                print("You: ", player)
                print("You LOSE")
            if comp == "rock":
                print("Comp: ", comp)
                print("You: ", player)
                print("You WIN")
        play_again = input("\nPlay Again? Y / N: ").lower()

        if play_again != "y":
            break
        print("\n")
    print("\nBye, See you some other time")
    # cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
    # random.shuffle(cards)  # This line will shuffle the items in the list

    # print(cards)


# rock_paper_scissors()


def exception_handling():
    # Exception is an event detected during execution that interrupt the flow of a program

    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    try:
        result = numerator / denominator
        # print(result)
    except ZeroDivisionError as e:
        print(e)
        print("You can't divide by Zero")
    except ValueError as e:
        print(e)
        print("Please Enter only numbers!!")
    except Exception as e:
        print(e)
        print("something went wrong")
    else:
        print(result)

    finally:
        print("\nThis will always execute.")


# exception_handling()


import os


def file():
    # Checking if a file exist
    path = "C:\\Users\\PRINCE\\Desktop\\folder"
    if os.path.exists(path):
        print("That location exists!")
        if os.path.isfile(path):
            print("This is a file")
        elif os.path.isdir(path):
            print("That is a directory")
    else:
        print("That location doesn't exist!!")


# file()

def create_a_file():
    try:
        with open('test.txt', 'x') as file:
            print("File Created successfully.")
    except FileExistsError:
        print("File with same name already Exist")


# create_a_file()

text = "This is Me testing write function again\n"
app = "This part of the text will append to the end of existing text"


def write_a_file():
    loc = 'test.txt'
    if os.path.exists(loc):
        with open('test.txt', 'w') as file:
            file.write(text)
            print("File has been overwritten with text.")
        with open('test.txt', 'a') as file:
            file.writelines(app)
            print("App text has been appended to the end of file")
    else:
        print("File not found")


# write_a_file()


def read_a_file():
    try:
        with open("test.txt", 'r') as files:
            print(files.read())
    except FileNotFoundError:
        print("The file was not found!")

    print(files.closed)


# read_a_file()


import shutil


# First import shutil into your program before using the copy function
# copyfile() = copies content of a file
# copy() = does the function of copyfile + permission mode + destination
# copy2() = does the function of copy() + copies metadata(file's creation and modification times)


def copy_a_file():
    shutil.copyfile('test.txt', 'copy.txt')
    shutil.copy('test.txt', 'copy.txt')
    shutil.copy2('test.txt', 'copy.txt')


# copy_a_file()


def move_a_file():
    source = "copy.txt"
    destination = "C:\\Users\\PRINCE\\Desktop\\copy.txt"
    try:
        if os.path.exists(destination):
            print("There's already a file there")
        else:
            os.replace(source, destination)
            print(source, " was moved")
    except FileNotFoundError:
        print(source, "was not found")


# move_a_file()


def del_a_file():
    path = 'copy.txt'
    path2 = "folder"
    path3 = "folder2"
    try:
        os.remove(path)  # This function deletes a file
        print("File Deleted Successfully")
        os.rmdir(path2)  # This deletes an empty directory
        print("Folder Deleted Successfully")
        shutil.rmtree(path3)  # This deletes directories that contains files
        print("Folder with files Deleted Successfully")
    except FileNotFoundError:
        print("That File was not found.")
    except PermissionError:
        print("You do not have permission to delete the directory")
    except OSError:
        print("The directory you're trying to delete is not empty")


# del_a_file()


def modules():
    # Module is a file that contain python code, may contain functions, classes etc.
    # It is used with modular programming, which is to separate a program into parts.
    import messages
    messages.hello()
    messages.bye()
    import messages as msg
    msg.bye()
    from messages import hello
    hello()
    help("modules")


# modules()


def new_game():
    guesses = []
    correct_guess = 0
    qst_num = 1

    for key in questions:
        print("----------------------")
        print(key)

        for i in options[qst_num - 1]:
            print(i)

        guess = input("\nEnter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guess += check_answer(questions.get(key), guess)
        qst_num += 1

    score(correct_guess, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("\nCORRECT")
        return 1
    else:
        print("\nWRONG")
        return 0


def score(correct_guess, guess):
    print("----------------------")
    print("RESULTS")
    print("----------------------")
    print("Answers: ", end=" ")

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")

    for i in guess:
        print(i, end=" ")
    print()

    point = int(correct_guess / len(questions) * 100)
    print("Your Score is: " + str(point) + "%")


def play_again():
    response = input("Do you want to play again? (Y/N): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False


questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python is attributed to which comedy group? ": "C",
    "What is the shape of  the earth? ": "D"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. Circle", "B. Square", "C. Triangle", "D. Sphere"]]


def end():
    while play_again():
        print()
        new_game()

    print("\nBye See You Later")


# new_game()
# end()


# Object--Oriented Programme
def OOP():
    from Cars import Car

    car1 = Car("Toyota", "Camry", 2022, "Grey")
    car2 = Car("Ford", "Mustang", 2023, "White")

    print(car1.make)
    print(car1.model)
    print(car1.year)
    print(car1.color)

    car1.drive()
    car2.stop()


# OOP()


# Class Variables

def ClassVar():
    from Cars import Car

    car1 = Car("Toyota", "Camry", 2022, "Grey")
    car2 = Car("Ford", "Mustang", 2023, "White")

    car1.wheels = 2
    Car.wheels = 2

    print(car1.wheels)
    print(car2.wheels)
    print(Car.wheels)


# ClassVar()


# INHERITANCE

def inheritance():
    pass



inheritance()