'''
Suppose you're on a game show, and you are given the choice of three doors: Behind
one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who
knows what is behind the doors, opens another door, say No. 3, which has a goat. He
then asks, "Do you want to pick door No. 2?" Is it to your advantage to switch your
choice?


Ans: ref {Monty Hall Problem}
'''

from random import randint, choice

def montyHall(switch: bool):
    doors = [0, 0, 0]
    winPos = randint(0, 2) # chooses one 0 to be winning
    doors[winPos] = 1 # makes it 1

    playerChoice = randint(0, 2)# randomly choose a door

    # the door to be revealed shouldn't be our choice or be winning
    remaining = [i for i in range(3) if i != playerChoice and doors[i] != 1]
    hostOpens = choice(remaining)

    if switch:
        playerChoice = [i for i in range(3) if i!=playerChoice and i!=hostOpens][0]
    
    return doors[playerChoice] == 1 # True if win, else false

def simulateTrials(n, switch):
    wins = 0
    for _ in range(n):
        if montyHall(switch):
            wins += 1

    return wins/n # percentage of wins

# run n trials
trials = 100
noSwitch = simulateTrials(trials, switch=False)
Switch = simulateTrials(trials, switch=True)

print(f"Yes Switch : {Switch*100}%\nNo Switch  : {noSwitch*100}%")

