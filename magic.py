import random

class Spell:

    def __init__(self, name, cost, prop, type, element):
        self.name = name
        self.cost = cost
        self.prop = prop
        self.type = type
        self.element = element

    def generate_spell_prop(self):
        low = self.prop - 15
        high = self.prop + 15
        return random.randrange(low, high)

    def get_spell_name(self):
        return name