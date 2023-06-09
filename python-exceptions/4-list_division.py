#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0
            division_result = num1 / num2 if num2 != 0 else 0
            result.append(division_result)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
    return result