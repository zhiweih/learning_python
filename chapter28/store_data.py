import shelve

from person import Person
from manager import Manager

def store_in_shelve():
    bob = Person('Bob', job='Software Engineer', pay=150000, ladder=2)
    jack = Manager('Jack', pay=300000, ladder=5)
    jack.promote(bob)

    db = shelve.open('person.db')
    for person in (bob, jack):
        db[person.name] = person
    db.close()

if __name__ == '__main__':
    store_in_shelve()
    db = shelve.open('person.db')
    print(db['Bob'])
    print(db['Jack'])
    db.close()
