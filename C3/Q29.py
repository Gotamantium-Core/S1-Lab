'''
Write a program to play a sticks game in which there are 16 sticks. Two players take
turns to play the game. Each player picks one set of sticks (needn't be adjacent) during
his turn. A set contains 1, 2, or 3 sticks. The player who takes the last stick is the loser.
The number of sticks in the set is to be input.
'''

running = True
player1Turn = True

sticks = 16
displaySticks = ["|"]*sticks

print(displaySticks)

while running:
    while player1Turn:
        print("--"*20)
        print("Player 1")
        p1 = int(input("Enter number of sticks to be removed: "))
        if p1 not in (1, 2, 3):
            print("Can only remove 1, 2, or 3 sticks")
            continue
        elif p1 > sticks:
            print("Too many sticks")
            continue
        elif p1 == sticks:
            print("You can't remove all sticks.\nRemove one less")
            continue
        else:
            sticks -= p1
            if sticks == 1:
                print("Player 1 has won")
                quit()

            print(displaySticks[:sticks])
            print(f"{sticks} sticks left")
            player1Turn = False;

    while not player1Turn: # player 2 turn
        print("--"*20)
        print("Player 2")
        p2 = int(input("Enter number of sticks to be removed: "))
        if p2 not in (1, 2, 3):
            print("Can only remove 1, 2, or 3 sticks")
            continue
        elif p2 > sticks:
            print("Too many sticks")
            continue
        elif p2 == sticks:
            print("You can't remove all sticks.\nRemove one less")
            continue
        else:
            sticks -= p2
            if sticks == 1:
                print("Player 2 has won")
                quit()

            print(displaySticks[:sticks])
            print(f"{sticks} sticks left")
            player1Turn = True;
