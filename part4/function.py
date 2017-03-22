def adder(*args):
    if len(args) == 0:
        return
    else:
        ret = args[0];
        for value in args[1:]:
            ret += value
        return ret

def kadder(**kargs):
    if len(kargs) == 0:
        return
    else:
        ret = None
        for key in kargs:
            ret = kargs[key] if ret == None else ret + kargs[key]
        return ret

def copyDict(old):
    ret = {}
    for key in old:
        ret[key] = old[key]
    return ret

def addDict(dict1, dict2):
    ret = {}
    for key in dict1:
        ret[key] = dict1[key]
    for key in dict2:
        ret[key] = dict2[key]
    return ret

def addDict2(dict1, dict2):
    ret = {}
    for key in set(dict1.keys()) | set(dict2.keys()):
        ret[key] = dict1.get(key, dict2.get(key))
    return ret

def is_prime(value):
    factor = value // 2
    while factor > 1:
        if value % factor == 0:
            print(value, 'has factor', factor)
            break
        factor -= 1
    else:
        print(value, 'is prime')

L = [2, 3, 5, 7, 11, 13]

import math

def sqrt_list(seq):
    return [math.sqrt(value) for value in seq]

def sqrt_list2(seq):
    return list(map(math.sqrt, seq))

def sqrt_list3(seq):
    ret = []
    for value in seq:
        ret.append(math.sqrt(value))
    return ret

import timeit
def time_sqrt(num):
    print(min(timeit.repeat('math.sqrt(%s)' % num, 'import math', repeat=5)))
    print(min(timeit.repeat('pow(%s, 0.5)' % num, repeat=5)))
    print(min(timeit.repeat('%s ** 0.5' % num, repeat=5)))

def countdown_recursive(num):
    print(num)
    if num == 0: return
    recursive_countdown(num - 1)

def factorial_recursive(num):
    return 1 if num == i else num * recursive_factorial(num - 1)

from functools import reduce
def factorial_reduce(num):
    return reduce(lambda x,y: x * y, range(1, num + 1))
