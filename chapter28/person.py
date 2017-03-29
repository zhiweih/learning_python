from attr_display import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0, ladder=1):
        self.name = name
        self.job = job
        self.pay = pay
        self.ladder = ladder

    def last_name(self):
        return self.name.split()[-1]

    def give_rasie(self, percentage):
        self.pay *= 1 + percentage
