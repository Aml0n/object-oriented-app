# applying_oop
# learned from Corey Schafer's video
import time as tm

class Player:
    def __init__(self, username, team, role):
        self.username = username
        self.team = team
        self.role = role
        self.health = 100 
        self.credits = 40

    def __str__(self):
        return f'{self.username} as {self.role}: {self.credits} credits'

    def RideLargeSubway(self):
        self.credits -= 10
        return
    
    def RideSmallSubway(self):
        self.credits -= 5
        return
    
    def RideBus(self):
        self.credits -= 5
        return
    
    def ChallengeComplete(self):
        self.credits += 10

    def run_action(self, action):
        if action == "RideLargeSubway":
            self.RideLargeSubway()
        elif action == "RideSmallSubway":
            self.RideSmallSubway()
        elif action == "RideBus":
            self.RideBus()
        elif action == "ChallengeComplete":
            self.ChallengeComplete()
        else:
            print("Invalid action")

    @staticmethod
    def StartGame():
        tm.sleep(10)
        print("sleep module works")


Player1 = Player('Aml0n', 'Blue', 'Chaser')
Player2 = Player('TestUser', 'Red', 'Runner')
#print(Player2.username)
#print(Player1.username)

# Player1.RideLargeSubway()
# print(Player1.credits)
# print(Player1)

# Example usage:
# Player1.run_action("RideLargeSubway")
# print(Player1.credits)
# Player1.run_action("ChallengeComplete")
# print(Player1.credits)

