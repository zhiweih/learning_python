class MyList:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return self.data + other

    def __radd__(self, other):
        return other + self.data

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

class MyListSub(MyList):
    add_count = 0

    def __init__(self, data):
        MyList.__init__(self, data)
        self.add_count = 0

    def __add__(self, other):
        MyListSub.add_count += 1
        self.add_count += 1
        return MyList.__add__(self, other)

    def __radd__(self, other):
        MyListSub.add_count += 1
        self.add_count += 1
        return MyList.__radd__(self, other)

    def class_add_count(self):
        print('Class add count:', MyListSub.add_count)

    def instance_add_count(self):
        print('Instance add count:', self.add_count)
