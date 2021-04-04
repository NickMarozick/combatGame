import random
from character import Character

#-----------------------------------------------------------------#
# BlueMen Constructor - updates name if input provided, otherwise defaults to BlueMen
#-----------------------------------------------------------------#

class BlueMen(Character):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.armor = 3
        self.strength = 12
        self.alive = True
        self.defender1 = True
        self.defender2 = True
        self.defender3 = True

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Blue Men"

#-----------------------------------------------------------------#
# BlueMen attack()- rolls for attack value
#-----------------------------------------------------------------#

    def attack(self, teamNum: int):
        rollOne = random.randrange(1,10)
        rollTwo = random.randrange(1,10)
        attackVal = rollOne + rollTwo

        print("TeamNum %d: BlueMen attack with: %d die roll\n" % (teamNum, attackVal))

        return attackVal

#-----------------------------------------------------------------#
# BlueMen::defense()- rolls for defense each turn. goes through some
# conditional statements to determine how many die to roll based on
# bools for each of the (3) potenital defenders being true or false
#-----------------------------------------------------------------#

    def defense(self, teamNum: int):
        rollDefense1 = 0
        rollDefense2 = 0
        rollDefense3 = 0

        if self.defender1:
            rollDefense1 = random.randrange(1, 6)
        if self.defender2:
            rollDefense2 = random.randrange(1, 6)
        if self.defender3:
            rollDefense3 = random.randrange(1, 6)

        defend = rollDefense1 + rollDefense2 + rollDefense3

        print("Team %d: BlueMen defending with: %d armor & %d strength\n" % (teamNum, self.armor, self.strength))
        print("Team %d: BlueMen's defensive effort: %d\n" % (teamNum, defend))

        return defend

#-----------------------------------------------------------------#
# BlueMen updateStrength(int)- updates strength value and returns bool value on if BlueMen is alive or not
#-----------------------------------------------------------------#

    def updateStrength(self, x: int, teamNum: int):

        self.strength = self.strength - x

        self.mob(teamNum)

        if self.strength < 1:
            self.defender1 = False
            print("Team %d: BlueMen is finished\n" % teamNum)
            self.alive = False
            return self.alive

        elif self.strength > 0:
            self.alive = True
            print("Team %d: BlueMen's updated strength: %d\n" % (teamNum, self.strength))

            return self.alive

#-----------------------------------------------------------------#
# BlueMen restore()- restores health post victory depending on conditional statements
#-----------------------------------------------------------------#

    def restore(self, teamNum: int):
        if self.strength > 8 and self.strength < 12:
            x = random.randrange(1,2)
            self.strength = self.strength + x
            if self.strength > 12:
                self.strength = 12
            print("Team %d: BlueMen's strength has been restored in full to %d strength\n" % (teamNum, self.strength))

        elif self.strength < 9 and self.strength > 4:
            self.strength = 9
            self.defender3 = True
            print("Team %d: Blue Men's strength has been restored to %d  strength. Blue Men Defender 3 was merely knocked out in battle and has revived post victory!\n" % (teamNum, self.strength))

        elif self.strength < 4 and self.strength > 0:
            self.strength = 6
            self.defender2 = True
            print("Team %d: Blue Men's strength was dangerously low. Blue Men Defender 2 was merely knocked out in battle and has revived post victory! Strength has been restored to %d strength\n" % (teamNum, self.strength))

#-----------------------------------------------------------------#
# BlueMen mob()- blueMen special function. based on strength points
# it determines how many defense rolls and adjusts the bools for defense
# function. For each 4 strength points lost, there is 1 less Blue Man
# and therefore 1 less defense roll. There are 3 blue men to start.
#-----------------------------------------------------------------#

    def mob(self, teamNum: int):
        if self.strength > 8:
            self.defender1 = True
            self.defender2 = True
            self.defender3 = True
            print("Team %d: BlueMen Full Strength Still\n" % teamNum)

        if self.strength < 9 and self.strength > 4:
            self.defender1 = True
            self.defender2 = True
            self.defender3 = False
            print("Team %d: BlueMen Man Down\n" % teamNum)

        if self.strength < 5 and self.strength > 0:
            self.defender1 = True
            self.defender2 = False
            self.defender3 = False
            print("Team %d: BlueMen Lone Soldier, Rambo Style\n" % teamNum)
