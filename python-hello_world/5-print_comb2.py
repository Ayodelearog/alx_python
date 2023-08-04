for number in range(100):
    if (number < 10):
        print("0"+"{}".format(number), sep=",", end=" ")
    else:
        print("{}".format(number), sep=",", end=" ")