import datetime

import attr


@attr.s
class Birth(object):
    date = attr.ib(type=datetime.datetime)

    def __str__(self):
        return str(self.date)


@attr.s
class Child(object):
    individual_id = attr.ib(type=str)


@attr.s
class Death(object):
    date = attr.ib(type=datetime.datetime)

    def __str__(self):
        return str(self.date)


@attr.s
class Divorce(object):
    date = attr.ib(type=datetime.datetime)

    def __str__(self):
        return str(self.date)


@attr.s
class FamilyChild(object):
    family_id = attr.ib(type=str)


@attr.s
class FamilySpouse(object):
    family_id = attr.ib(type=str)


@attr.s
class Husband(object):
    individual_id = attr.ib(type=str)

    def __str__(self):
        return str(self.individual_id)


@attr.s
class Marriage(object):
    date = attr.ib(type=datetime.datetime)

    def __str__(self):
        return str(self.date)


@attr.s
class Name(object):
    first = attr.ib(type=str)
    last = attr.ib(type=str)

    def __str__(self):
        return '{} /{}/'.format(self.first, self.last)


@attr.s
class Note(object):
    content = attr.ib(type=str)

    def __str__(self):
        return str(self.content)


@attr.s
class Sex(object):
    sex = attr.ib(type=str)

    def __str__(self):
        return self.sex


@attr.s
class Wife(object):
    individual_id = attr.ib(type=int)


@attr.s
class Family(object):
    id = attr.ib(type=str)
    children = attr.ib(factory=list, init=False)
    divorces = attr.ib(factory=list, init=False)
    husbands = attr.ib(factory=list, init=False)
    marriages = attr.ib(factory=list, init=False)
    wives = attr.ib(factory=list, init=False)

    @classmethod
    def from_tokens(cls, tokens):
        family = cls(tokens[1].value)
        # First two tokens are level and family ID
        # The rest should be model objects if the transformer is correct
        for obj in tokens[2:]:
            if isinstance(obj, Child):
                family.children.append(obj)
            elif isinstance(obj, Divorce):
                family.divorces.append(obj)
            elif isinstance(obj, Husband):
                family.husbands.append(obj)
            elif isinstance(obj, Marriage):
                family.marriages.append(obj)
            elif isinstance(obj, Wife):
                family.wives.append(obj)
            else:
                raise ValueError("Token we don't know about: {}"
                                 .format(repr(obj)))
        return family


@attr.s
class Individual(object):
    id = attr.ib(type=str)
    birth = attr.ib(type=Birth, init=False)
    death = attr.ib(type=Death, default=None, init=False)
    name = attr.ib(type=Name, init=False)
    sex = attr.ib(type=Sex, init=False)
    child_to = attr.ib(factory=list, init=False)
    spouse_to = attr.ib(factory=list, init=False)

    @classmethod
    def from_tokens(cls, tokens):
        individual = cls(tokens[1].value)
        # First two tokens are level and individual ID
        # The rest should be model objects if the transformer is correct
        for obj in tokens[2:]:
            if isinstance(obj, Birth):
                individual.birth = obj
            elif isinstance(obj, Death):
                individual.death = obj
            elif isinstance(obj, Name):
                individual.name = obj
            elif isinstance(obj, Sex):
                individual.sex = obj
            elif isinstance(obj, FamilyChild):
                individual.child_to.append(obj)
            elif isinstance(obj, FamilySpouse):
                individual.spouse_to.append(obj)
            else:
                raise ValueError("Token we don't know about: {}"
                                 .format(repr(obj)))
        return individual
