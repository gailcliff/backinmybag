import bisect


class Person:
    name: str
    gender: str
    age: int
    
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    

def user_key(person: Person):
    return person.age


class Sorter:
    items: list[Person]
    seek: int

    def __init__(self):
        self.items = []

        bisect.insort(self.items, Person('foo', 'male', 45), key=user_key)
        bisect.insort(self.items, Person('bar', 'female', 24), key=user_key)
        bisect.insort(self.items, Person('baz', 'male', 39), key=user_key)
        bisect.insort(self.items, Person('choo', 'male', 67), key=user_key)
        bisect.insort(self.items, Person('zoo', 'female', 14), key=user_key)
        bisect.insort(self.items, Person('loo', 'male', 21), key=user_key)
        bisect.insort(self.items, Person('moo', 'female', 89), key=user_key)
        bisect.insort(self.items, Person('var', 'male', 33), key=user_key)
        bisect.insort(self.items, Person('char', 'male', 31), key=user_key)
        bisect.insort(self.items, Person('lar', 'male', 6), key=user_key)

    def refresh_seek(self):
        self.seek = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if self.seek == 0:
            self.refresh_seek()
        self.seek -= 1
        return self.items[self.seek]


sorter = Sorter()


def next_lucky_persons() -> list[Person]:
    lucky_persons = [next(sorter) for i in range(3)]

    return lucky_persons
