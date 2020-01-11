#!python3
#-*-encoding:utf-8-*-


class BoolValues:
    def __init__(self, thing, reverse=False):
        self.thing = thing
        self.reverse = reverse

    def __getattr__(self, attr):
        setattr(
            self.thing,
            f"is_a_{attr}",
            True if not self.reverse else False
        )


class Thing:
    def __init__(self, name):
        self.name = name

        self.is_a = BoolValues(self)
        self.is_not_a = BoolValues(self, reverse=True)
        self.is_the = Parent(self)


class Property:
    def __init__(self, attr, mid, high):
        self.mid = mid
        self.high = high
        self.attr = attr

    def __getattr__(self, attr):
        self.high.mid.__setattr__(self.attr, attr)
        return Property(attr, self.mid, self)


class Parent:
    def __init__(self, mid):
        self.mid = mid

    def __getattr__(self, attr):
        return Property(attr, self.mid, self)


if __name__ == '__main__':
    jane = Thing('Jane')
    print(jane.name)    # => 'Jane'

    jane.is_a.person
    jane.is_a.woman
    jane.is_not_a.man
    print(jane.is_a_person) # => True
    print(jane.is_a_man)    # => False

    jane.is_the.parent_of.joe
    print(jane.parent_of)   # => 'joe'