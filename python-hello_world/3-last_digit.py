import random
number = random.randint(-10000, 10000)
numList = [int(i) for i in str(number)]
def lastDigitPrinter(number):
    firstWords = "Last digit of"
    lastDigit = numList[-1]
    if (lastDigit > 5):
        print(firstWords, number, "is", lastDigit, "and is greater than 5")
    elif (lastDigit == 0):
        print(firstWords, number, "is", lastDigit, "and is 0")
    elif (lastDigit < 6) and (lastDigit != 0):
        print(firstWords, number, "is", lastDigit, "and is less than 6 and not 0")

lastDigitPrinter(number)