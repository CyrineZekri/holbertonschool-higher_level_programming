#!/usr/bin/python3
def print_last_digit(number):

    if number > 0:
        x = number % 10
        print(x, end="")
        return (x)
    elif number < 0:
        x = (number * -1) % 10
        print(x, end="")
        return (x)
    else:
        x = 0
        return (x)
