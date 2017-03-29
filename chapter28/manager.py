from person import Person

class Manager(Person):
    def __init__(self, name, pay=0, num_promoted=0, ladder=0):
        Person.__init__(self,
                        name,
                        job='Manager',
                        pay=pay,
                        ladder=ladder)
        self.num_promoted = num_promoted

    def promote(self, person):
        person.ladder += 1
        self.num_promoted += 1
