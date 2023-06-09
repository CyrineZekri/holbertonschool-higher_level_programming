#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = len(my_list)
    if x == 0:
        return None
    else:
        new_list = ()
        for i in range(x):
            if (my_list[i] % 2) == 0:
                new_list = new_list + ('true',)
            else:
                new_list = new_list + ('false',)
        return (new_list)
