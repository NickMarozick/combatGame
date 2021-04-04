import random

class Character:
    def __init__(self, *inp):

        self.armor = 0
        self.strength = 0

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Unknown"

    def attack(self):
        return 0
    def defense(self):
        return 0
    def updateStrength(self, x:int):
        self.strength+=x
    def restore(self):
        return 0
