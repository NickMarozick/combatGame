from character import Character
from characters.vampire import Vampire
from characters.blueMen import BlueMen
from characters.barbarian import Barbarian
from characters.medusa import Medusa
from characters.harryPotter import HarryPotter
from collections import deque

class CombatGame:
    def __init__(self):
        self.team1Score = 0
        self.team2Score = 0
        self.team1Size = 0
        self.team2Size = 0
        self.team1Alive = deque()
        self.team2Alive = deque()
        self.team1Finished = deque()
        self.team2Finished = deque()

    def menuTeamSize(self):
        print("\nWelcome to Fantasy Combat CombatGame!\n")
        print("Pick the fighter amounts for your two teams\n")

        while self.team1Size < 1 or self.team1Size > 10:
            try:
                self.team1Size = int(input("Enter a fighter count for Team One between 1 and 10:  "))
            except:
                self.team1Size = 0

        while self.team2Size < 1 or self.team2Size > 10:
            try:
                self.team2Size = int(input("Enter a fighter count for Team Two between 1 and 10:  "))
            except:
                self.team2Size = 0

    def menuCharacterSelect(self):

        team1 = deque()
        team2 = deque()

        print("Select your characters for Team One!\n")

        for i in range(self.team1Size):
            team1.append(self.createCharacter(1))

        print("Select your characters for Team Two!\n")

        for j in range(self.team2Size):
            team2.append(self.createCharacter(2))

        return team1, team2


    def createCharacter(self, teamNum):
        print("Pick Team %s Character by selecting from below: \n" % teamNum)
        print("1) Vampire\n")
        print("2) Barbarian\n")
        print("3) BlueMen\n")
        print("4) Medusa\n")
        print("5) HarryPotter\n\n")

        choice = 0

        while choice !=1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
            try:
                choice = int(input("Input the character number that you select:  "))
            except:
                choice = 0

        characterName = input("Enter character name:  ")

        if choice is 1:
            character = Vampire(characterName)
            return character

        elif choice is 2:
            character = Barbarian(characterName)
            return character

        elif choice is 3:
            character = BlueMen(characterName)
            return character

        elif choice is 4:
            character = Medusa(characterName)
            return character

        elif choice is 5:
            character = HarryPotter(characterName)
            return character

    def battleOnevOne(self):
        if len(self.team1Alive) > 0 and len(self.team2Alive) > 0:

            print("################################################\n\n")

            # rolls for the attack and damage of each player
            player1Damage = self.team2Alive[0].attack(2) - self.team1Alive[0].defense(1) - self.team1Alive[0].armor
            player2Damage = self.team1Alive[0].attack(1) - self.team2Alive[0].defense(2) - self.team2Alive[0].armor

            if player1Damage < 1:
                print("Easily defended, no strength lost by Team 1 Fighter %s\n" % self.team1Alive[0].name)
                player1Damage = 0

            if player2Damage < 1:
                print("Easily defended, no strength lost by Team 2 Fighter %s\n" % self.team2Alive[0].name)
                player2Damage = 0

            if player1Damage > 0:
                print("%d damage inflicted to Team 1 Fighter %s\n" % (player1Damage, self.team1Alive[0].name))

            if player2Damage > 0:
                print("%d damage inflicted to Team 2 Fighter %s\n" % (player2Damage, self.team2Alive[0].name))

            # updateStrength
            fighterAliveTeam1 = self.team1Alive[0].updateStrength(player1Damage, 1)
            fighterAliveTeam2 = self.team2Alive[0].updateStrength(player2Damage, 2)


            print("--------------------------------------------------\n\n")

            if fighterAliveTeam1 == False or fighterAliveTeam2 == False:
                self.reOrderLineUp()

        else:
            # gameOver
            self.gameOver()


    def reOrderLineUp(self):
        if self.team1Alive[0].alive is True and self.team2Alive[0].alive is False:
            # add to team finished queue and remove from live players
            self.team2Finished.append(self.team2Alive.popleft())

            # restore winning player
            self.team1Alive[0].restore(1)
            # put winning player at the back of the lineup
            self.team1Alive.append(self.team1Alive.popleft())
            # add to score
            self.team1Score+=1

        elif self.team2Alive[0].alive is True and self.team1Alive[0].alive is False:
            # add to team finished queue and remove from live players
            self.team1Finished.append(self.team1Alive.popleft())

            # restore winning player
            self.team2Alive[0].restore(2)
            # put winning player at the back of the lineup
            self.team2Alive.append(self.team2Alive.popleft())
            # add to score
            self.team2Score+=1

        elif self.team1Alive[0].alive is False and self.team2Alive[0].alive is False:
            # add to team finished queue and remove from live players)
            self.team1Finished.append(self.team1Alive.popleft())
            self.team2Finished.append(self.team2Alive.popleft())
            #update both scores
            self.team1Score+=1
            self.team2Score+=1


    def checkValidTeams(self):
        if len(self.team1Alive) < 1 or len(self.team2Alive) < 1:
            return False
        else:
            return True

    def gameOver(self):
        if self.team1Score == self.team2Score:
            print("The battle ended in a stalemate - DRAW\n")

        elif self.team1Score > self.team2Score:
            "Team 1 is the battle champion!\n"

        elif self.team2Score > self.team1Score:
            "Team 2 is the battle champion!\n"

        print("Team 1 Score: %d \n" % self.team1Score)
        print("Team 2 Score: %d \n" % self.team2Score)


    def resetGame(self):
        # empty the character queues

        while len(self.team1Alive) > 0:
            self.team1Alive.pop()
        while len(self.team2Alive) > 0:
            self.team2Alive.pop()
        while len(self.team1Finished) > 0:
            self.team1Finished.pop()
        while len(self.team2Finished) > 0:
            self.team2Finished.pop()

        # reset scores
        self.team1Score = 0
        self.team2Score = 0

        # reset team size
        self.team1Size = 0
        self.team2Size = 0

    def playAgain(self):
        print("Would you like to play again? \n")
        play = 0
        while play!= 1 and play!= 2:
            play =  int(input("Enter 1: Play Again\nEnter 2: Quit\n"))

        if play == 1:
            self.playCombatGame()

        if play == 2:
            print("\nThanks for playing the combat game!\n")
            quit()

    def playCombatGame(self):
        self.menuTeamSize()

        self.team1Alive, self.team2Alive = self.menuCharacterSelect()

        while self.checkValidTeams() is True:
            self.battleOnevOne()

        self.gameOver()

        self.resetGame()

        self.playAgain()
