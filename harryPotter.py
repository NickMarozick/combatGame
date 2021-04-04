import random
from character import Character

class HarryPotter(Character):
    def __init__(self, *inp):
        super().__init__(*inp)
        self.armor = 0
        self.strength = 10
        self.alive = True
        self.firstLife = True

        if len(inp) > 0:
            self.name = inp[0]

        else:
            self.name = "Harry Potter"

# Harry Potter attack function
    def attack(self, teamNum: int):
        rollOne = random.randrange(1, 6)
        rollTwo = random.randrange(1, 6)

        attackVal= rollOne+rollTwo

        print("Team %d: Harry Potter Attack with: %d die roll\n" % (teamNum, attackVal))

        return attackVal

# Harry Potter Defense function
    def defense(self, teamNum: int):
        rollDefense1 = random.randrange(1, 6)
        rollDefense2 = random.randrange(1, 6)

        defend = rollDefense1 + rollDefense2

        print("Team %d: Harry Potter defending with: %d armor & %d strength\n" % (teamNum, self.armor, self.strength))
        print("Team %d: Harry's defensive effort: %d\n" % (teamNum, defend))

        return defend

    # def updateStrength, Harry Pitter has additional powers to rise from the dead on his first firstLife

    def updateStrength(self, x: int, teamNum: int):

        self.strength = self.strength - x

        if self.strength < 1 and self.firstLife is True:
            print("Team %d: Harry's updated strength: %d\n" % (teamNum, self.strength))
            self.firstLife= False
            self.Hogwarts(teamNum)
            self.alive = True
            print("Team %d: Harry's updated strength: %d\n" % (teamNum, self.strength))

            return self.alive

        if self.strength > 0:
            self.alive = True
            print("Team %d: Harry's updated strength: %d\n" % (self.strength, teamNum))

            return self.alive

        if self.strength < 1 and self.firstLife is False:
            print("Team %d: Harry's updated strength: %d\n" % (teamNum, self.strength))
            print("Team %d: HarryPotter is finished. A deed not even Voldemort could accomplish\n" % teamNum)
            self.alive = False

            return self.alive

        # Hogwarts this function is called from updateStrength() based on bool firstLife being true. if so, firstLife is later set to false, however Harry is revived from death and strength is now doubled to 20. There is only one life revive
    def Hogwarts(self, teamNum: int):
        print("Team %d: HarryPotter surely couldn't have came back from that....But he did! Saved by the phoenix! He's back for vengeance this time\n" % teamNum)
        self.strength = 20


    def restore(self, teamNum: int):
        if self.strength ==  9:
            self.strength = 10
            print("Team %d: Strength has been restored to 10 after the victory\n" % teamNum)

        elif self.strength < 9:
            randIncrease = random.randrange(1, 3)
            self.strength = self.strength + randIncrease

            if self.strength > 10:
                self.strength = 10

            print("Team %d: After victory Harry's strength has increased to %d\n" % (teamNum, self.strength))

        else:
            print("Team %d: No additional health restored to Harry after the victory\n" % teamNum)
