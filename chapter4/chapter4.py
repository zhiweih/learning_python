import math

def number_demo():
    print('Number:')
    value_helper('5 / 4')
    value_helper('5 // 4')
    value_helper('2 ** 10000')
    value_helper('math.pi')
    print()

s = '你好，世界！'
def string_demo():
    print('String:')
    value_helper('s')
    value_helper('s.encode("utf8")')
    value_helper('s[0]')
    value_helper('s[-1]')
    value_helper('s[1:2]')
    value_helper('len(s)')
    value_helper('s * 3')
    value_helper('list(s)')
    value_helper('"".join(list(s))')
    value_helper('"{:,.2f}".format(1002.345)')
    value_helper('ord("s")')
    value_helper('dir(s)')
    statement_helper('help(s.partition)')
    print()

l = [123, '程序', [9, 8 , None, {}]]
ret = None
def list_demo():
    print('List:')
    value_helper('l')
    statement_helper('l.append("something")')
    value_helper('l')
    statement_helper('l.pop(1)')
    value_helper('l')
    statement_helper('l.reverse()')
    value_helper('l')
    value_helper('[value ** 2 for value in range(5)]')
    value_helper('[(value + 1, value - 1) for value in range(5)]')
    value_helper('{value for value in range(5)}')
    value_helper('{x: ord(x) for x in "deliberation"}')
    value_helper('sum(range(5))')
    print()

def dictionary_demo():
    print('Dictionary:')
    value_helper('dict(zip(["name", "age"], ["bob", 42]))')
    value_helper('"a" in dict(a=42)')
    value_helper('dict(a=42).get("x", 16)')
    value_helper('sorted({"x": 1, "y": 2, "a": 3})')
    print()

def value_helper(code):
    value = eval(code)
    template = None
    if type(value) == float:
        template = '%f'
    elif type(value) == int:
        template = '%d'
    elif type(value) == bool:
        template = '%s'
    else:
        template = '"%s"'

    print(code, ' = ', template % eval(code))

def statement_helper(code):
    print()
    print('The result for:')
    print(code)
    print()
    eval(code)
    print()

number_demo()
string_demo()
list_demo()
dictionary_demo()
