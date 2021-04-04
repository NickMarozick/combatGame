import random
from character import Character

#-----------------------------------------------------------------#
# Vampire Constructor - updates name if input provided, otherwise defaults to Vampire
#-----------------------------------------------------------------#

class Vampire(Character):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.armor = 1
        self.strength = 18
        self.alive = True

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Vampire"

#-----------------------------------------------------------------#
# Vampire attack()- rolls for attack value
#-----------------------------------------------------------------#

    def attack(self, teamNum: int):
        attackVal = random.randrange(1,12)

        print("Team %d: Vampire attack with: %d die roll\n" % (teamNum, attackVal))

        return attackVal

#-----------------------------------------------------------------#
# Vampire defense()- rolls for defense value
#-----------------------------------------------------------------#

    def defense(self, teamNum: int):
        defend = random.randrange(1, 6)

        print("Team %d: Vampire defending with: %d armor & %d strength\n" % (teamNum, self.armor, self.strength))
        print("Team %d: Vampire's defensive effort: %d\n" % (teamNum, defend))

        return defend

#-----------------------------------------------------------------#
# Vampire charm()- adjusts bool value used by defend. 50/50 chance
# at charming opponent, where vampire takes doesn't take any damage if charmed
# is equal to true
#-----------------------------------------------------------------#

    def charm(self, teamNum: int):
        roll = random.randrange(1, 2)

        if roll == 1:
            charmed = True
            print("Team %d: Vampire has charmed this round\n" % teamNum)

        if roll == 2:
            charmed= False

        return charmed

#-----------------------------------------------------------------#
# Vampire updateStrength(int)- updates strength value and returns bool value on if Vampire is alive or not
#-----------------------------------------------------------------#

    def updateStrength(self, x: int, teamNum: int):

        charmed = self.charm(teamNum)

        self.strength = self.strength - x

        if self.strength > 0 and charmed == False:
            self.strength = self.strength - x

        if self.strength > 0 and charmed == True:
            self.alive = True
            print("Team %d: The vampire has charmed it's opponent. The attacker has forgotten his fury this turn. No damage taken\n" % teamNum)

        if self.strength < 1:
            print("Team %d: Vampire is finished. The Transylvanians rejoice!\n" % teamNum)
            self.alive = False
            return self.alive

        print("Team %d: Vampire's updated strength: %d\n" % (teamNum, self.strength))
        return self.alive

#-----------------------------------------------------------------#
# Vampire restore()- restores health post victory depending on conditional statements
#-----------------------------------------------------------------#

    def restore(self, teamNum:int):
        if self.strength > 12 and self.strength < 18:
            randIncrease = random.range(1, 6)
            self.strength = self.strength + randIncrease

            if self.strength > 18:
                self.strength = 18
                print("Team %d Fighter: Vampire's strength has been restored to %d after the victory\n" % (teamNum, self.strength))
            else:
                print("Team %d Fighter: Vampire's strength has been restored to %d after the victory\n" % (teamNum, self.strength))

        elif self.strength < 13 and self.strength > 6:
            randIncrease = random.randrange(1, 6)
            self.strength = self.strength + randIncrease
            print("Team %d Fighter: Vampire's strength has been restored to %d after the victory\n" % (teamNum, self.strength))

        elif self.strength < 7 and self.strength > 0:
            randIncrease = random.range(1, 9)
            self.strength = self.strength + randIncrease

            print("Team %d Fighter: The vampires health was low after victory. After a blood feast his strength has been restored to %d\n" % (teamNum, self.strength))
