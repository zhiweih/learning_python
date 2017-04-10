class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        return Set([el for el in self.data if el in other])

    def union(self, other):
        res = self.data[:]
        for el in other:
            if not el in res:
                res.append(el)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        print('in __len__')
        return len(self.data)
    def __getitem__(self, key):
        print('in __getitem__')
        return self.data[key]
    def __and__(self, other):
        print('in __and__')
        return self.intersect(other)
    def __or__(self, other):
        print('in __or__')
        return self.union(other)
    def __repr__(self):
        print('in __repr__')
        return 'Set:' + repr(self.data)
    def __iter__(self):
        print('in __iter__')
        return iter(self.data)

class SubSet(Set):
    def __init__(self, value=[]):
        Set.__init__(self, value)

    def intersect(self, *args):
        res = self
        for x in args:
            res = Set.intersect(res, x)
        return res

    def union(self, *args):
        res = self
        for x in args:
            res = Set.union(res, x)
        return res

    def concat(self, *args):
        res = self
        for x in args:
            res = Set.concat(res, x)
        return res

    def __add__(self, other):
        res = SubSet(self.data[:])
        res.concat(other)
        return res

    def __getattr__(self, name):
        return getattr(self.data, name)
