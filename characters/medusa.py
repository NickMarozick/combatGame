import random
from character import Character

#-----------------------------------------------------------------#
# Medusa Constructor - updates name if input provided, otherwise defaults to Medusa
#-----------------------------------------------------------------#

class Medusa(Character):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.armor = 3
        self.strength = 8
        self.alive = True

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Medusa"


#-----------------------------------------------------------------#
# Medusa attack()- rolls for attack value. If 12 is rolled, glare special ability is called
#-----------------------------------------------------------------#

    def attack(self, teamNum: int):
        rollOne = random.randrange(1,6)
        rollTwo = random.randrange(1,6)
        attackVal = rollOne + rollTwo

        if attackVal == 12:
            attackVal = self.glare(teamNum)
            print("Team %d: Medusa Glare attack with: %d damage. No one's looked Medusa in the eyes and lived to tell the tale...\n" % (teamNum, attackVal))
            return attackVal

        if attackVal < 12:
            print("Team %d: Medusa standard attack with: %d die roll\n" % (teamNum, attackVal))

        return attackVal


#-----------------------------------------------------------------#
# Medusa defense()- rolls once for defense value
#-----------------------------------------------------------------#

    def defense(self, teamNum: int):
        defend = random.randrange(1, 6)

        print("Team %d: Medusa defending with: %d armor & %d strength\n" % (teamNum, self.armor, self.strength))
        print("Team %d: Medusa's defensive effort: %d\n" % (teamNum, defend))

        return defend

#-----------------------------------------------------------------#
# Medusa updateStrength(int)- updates strength value and returns bool value on if Medusa is alive or not
#-----------------------------------------------------------------#

    def updateStrength(self, x: int, teamNum: int):

        self.strength = self.strength - x

        if self.strength < 1:
            print("Team %d: Medusa is finished\n" % teamNum)
            self.alive = False
            return self.alive

        elif self.strength > 0:
            self.alive = True
            print("Team %d: Medusa's updated strength: %d\n" % (teamNum, self.strength))

            return self.alive

#-----------------------------------------------------------------#
# Medusa restore()- restores health post victory depending on conditional statements
#-----------------------------------------------------------------#

    def restore(self, teamNum: int):
        if self.strength > 5 and self.strength < 8:
            self.strength = 8
            print("Team %d: Medusa's strength has been restored in full to %d strength\n" % (teamNum, self.strength))

        elif self.strength < 6 and self.strength > 0:
            randIncrease = random.randrange(1,5)
            self.strength = self.strength + randIncrease

            if self.strength > 8:
                self.strength = 8

            print("Team %d: Medusa's health has been restored to %d strength\n" % (teamNum, self.strength))

#-----------------------------------------------------------------#
# Medusa glare()- sets attack value to 100, only called when die roll of attack=12
#-----------------------------------------------------------------#

    def glare(self, teamNum: int):
        print("Team %d: Glare! Enemy was turned to stone! Should have avoided the eyes....\n" % teamNum)
        attackVal = 100
        return attackVal
