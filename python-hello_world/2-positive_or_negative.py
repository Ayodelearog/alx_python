import random
number = random.randint(-10, 10)


def signChecker(number):
    if (number > 0):
        print(number, "is positive")
    elif (number == 0):
        print(number, "is zero")
    else:
        print(number, "is negative")


signChecker(number)
