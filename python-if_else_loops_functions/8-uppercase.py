#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in range(len(str)):
        if (ord(str[i]) in range(97, 123)):
            upper += chr(ord(str[i]-32))
        else:
            upper += str[i]
    print("{}".format(str))
