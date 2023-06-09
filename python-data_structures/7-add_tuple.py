#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        x = tuple_a[0] + tuple_b[0]
        y = tuple_a[1] + tuple_b[1]
        result = (x, y)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        x = tuple_a[0] + tuple_b[0]
        result = (x, 0)
    elif len(tuple_a) >= 2 and len(tuple_a) == 0:
        result = (tuple_a[0], tuple_a[1])
    elif len(tuple_b) == 0 and len(tuple_a) >= 2:
        result = (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        result = (tuple_a[0]+tuple_b[0], tuple_b[1])
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        result = (tuple_a[0]+tuple_b[0], tuple_a[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        result = (tuple_b[0], 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        result = (tuple_a[0], 0)
    return result
