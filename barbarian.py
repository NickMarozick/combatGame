import random
from character import Character

#-----------------------------------------------------------------#
# Barbarian Constructor - updates name if input provided, otherwise defaults to Barbarian
#-----------------------------------------------------------------#

class Barbarian(Character):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.armor = 0
        self.strength = 12
        self.alive = True

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Barbarian"

#-----------------------------------------------------------------#
# Barbarian attack()- rolls for attack value
#-----------------------------------------------------------------#

    def attack(self, teamNum: int):
        rollOne = random.randrange(1,6)
        rollTwo = random.randrange(1,6)
        attackVal = rollOne + rollTwo

        print("Team %d: Barbarian attack with: %d die rol\n" % (teamNum, attackVal))

        return attackVal

#-----------------------------------------------------------------#
# Barbarian defense()- rolls for defense value
#-----------------------------------------------------------------#

    def defense(self, teamNum: int):
        rollDefense1 = random.randrange(1, 6)
        rollDefense2 = random.randrange(1, 6)

        defend = rollDefense1 + rollDefense2

        print("Team %d: Barbarian defending with: %d armor & %d strength\n" % (teamNum, self.armor, self.strength))
        print("Team %d: Barbarian's defensive effort: %d\n" % (teamNum, defend))

        return defend

#-----------------------------------------------------------------#
# Barbarian updateStrength(int)- updates strength value and returns bool value on if barbarian is alive or not
#-----------------------------------------------------------------#

    def updateStrength(self, x: int, teamNum: int):

        self.strength = self.strength - x

        if self.strength < 1:
            print("Team %d: Barbarian is finished\n" % teamNum)
            self.alive = False
            return self.alive

        elif self.strength > 0:
            self.alive = True
            print("Team %d: Barbarian's updated strength: %d\n" % (teamNum, self.strength))

            return self.alive

#-----------------------------------------------------------------#
# Barbarian restore()- restores health post victory depending on conditional statements
#-----------------------------------------------------------------#

    def restore(self, teamNum: int):
        if self.strength > 9 and self.strength < 12:
            self.strength = 12
            print("Team %d: Barbarian's strength has been restored in full to %d strength\n" % (teamNum, self.strength))

        elif self.strength < 10:
            randIncrease = random.randrange(1,4)
            self.strength = self.strength + randIncrease

            if self.strength > 12:
                self.strength = 12


            print("Team %d: Barbarians health has been restored to %d strength\n" % (teamNum, self.strength))
