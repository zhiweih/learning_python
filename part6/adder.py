class Adder:
    def __init__(self, data):
        self.data = data

    def add(self, x, y):
        print('Not implemented')

    def __add__(self, other):
        return self.add(self.data, other)

    __radd__ = __add__

class ListAdder(Adder):
    def __init__(self, data):
        Adder.__init__(self, data)

    def add(self, x, y):
        return x + y

"""
This won't work for 2 DictAdder instances.
"""
class DictAdder(Adder):
    def __init__(self, data):
        Adder.__init__(self, data)

    def add(self, x, y):
        res = x.copy()
        res.update(y)
        return res
