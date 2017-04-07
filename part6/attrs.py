# Doesn't work for dunder methods in python 3.x
class Attrs:
    def __getattr__(self, name):
        print('Getting:', name)

    def __setattr__(self, name, value):
        print('Setting:', name, 'with:', value)
