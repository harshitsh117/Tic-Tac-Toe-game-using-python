#Tic-Tac_toe 
#Printing Title of our game
print("Tic-Tac-Toe")

#Importing packages
import random
import time

#Asking for players names
player1 = input("Enter player 1's name : ")
player2 = input("Enter player 2's name : ")

#Assigning characters to both players
print("\nplayer 1's character is x")
print("player 2's character is o\n")

#dDeciding who will mark first through tossing
print("\nTossing...\n")

time.sleep(2)      #Making a puase for toss

markedPos = []

#Algorithm of tossing


if random.randint(0,1)==0:
    toss = 0
else:
    toss = 1

#Declaring the results of toss
if toss==0:
    print(player1," won the Toss")
    print(player1," will write first\n")
else:
    print(player2," won the Toss")
    print(player2," will write first\n")



#posArray is made just to show the positions
#to mark the characters
posArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        print(posArray[i][j],end="  ")
    print("")

#gameArray, in this array game will be played
gameArray = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
for i in range(3):
    for j in range(3):
        print(gameArray[i][j],end="  ")
    print("")
print("")

def result(value):
    #Checking character with players characters
    if value == "x":
        print(player1," won")
        return 1
    elif value == 'o':
        print(player2," won")

        #returning value for stopGame variable
        return 1


def check():
    #Chick function is to find if user won by checking below conditions
    if gameArray[0][0] == gameArray[0][1] == gameArray[0][2]:
        #sinding character to the result funvtion to find out which player won the game

        # returning value for stopGame variable
        return result(gameArray[0][0])

    if gameArray[1][0] == gameArray[1][1] == gameArray[1][2]:
        # returning value for stopGame variable
        return result(gameArray[1][0])

    if gameArray[2][0] == gameArray[2][1] == gameArray[2][2]:
        # returning value for stopGame variable
        return result(gameArray[2][0])

    if gameArray[0][0] == gameArray[1][0] == gameArray[2][0]:
        # returning value for stopGame variable
        return result(gameArray[0][0])

    if gameArray[0][1] == gameArray[1][1] == gameArray[2][1]:
        # returning value for stopGame variable
        return result(gameArray[0][1])
    if gameArray[0][2] == gameArray[1][2] == gameArray[2][2]:
        # returning value for stopGame variable
        return result(gameArray[0][2])

    if gameArray[0][0] == gameArray[1][1] == gameArray[2][2]:
        # returning value for stopGame variable
        return result(gameArray[0][0])

    if gameArray[0][2] == gameArray[1][1] == gameArray[2][0]:
        return result(gameArray[0][2])

 #using this function to mark characters on respective positions
def settingValue(index, character):
    #using filledPos array to check wether the pos is already filled or not

    # Creating an arrray named filledPos
    # for ensuring that no overrwriting of charcaters occurs

    if index in markedPos:
        #Asking user to not to mark on already marked positionso
        index=int(input("\nError : Position already filled. Choose another position :"))
        while index  in markedPos:
            index = int(input("\nError : Position already filled. Choose another position :"))

    #adding already marked positions to markedPos array
    markedPos.append(index)

    #marking user's characters to the gamesArray using their index positions
    if index == 1:
        gameArray[0][0] = character

    if index == 2:
        gameArray[0][1] = character

    if index == 3:
        gameArray[0][2] = character

    if index == 4:
        gameArray[1][0] = character

    if index == 5:
        gameArray[1][1] = character

    if index == 6:
        gameArray[1][2] = character

    if index == 7:
        gameArray[2][0] = character

    if index == 8:
        gameArray[2][1] = character

    if index == 9:
        gameArray[2][2] = character


    #calling Chack function
    return check()

if __name__ == '__main__':

    count = 1

    #declaring a variable named  stopGame, which will be used to stop the game if one of the user wins
    stopGame=0
    #running a for loop 9 times as we have 9 positions to mark
    #on each loop program will ask a position from user to mark character
    for i in range(9):
        #if toss=1 that means player1 has won so he will get to mark
        #his character first
        if toss==1:
            #using count variable to ask positions from both the users
            #one-by-one
            if count == 1:
                character = 'o'
                index = int(input("player2 enter your index:"))
                stopGame = settingValue(index, character)   #receiving value for stopGame variable
                count = -1
            else:
                count = 1
                character = 'x'
                index = int(input("\nplayer1 enter your index:"))
                stopGame = settingValue(index, character)

        # if toss=1 that means player1 has won so he will get to mark
        # his character first
        elif toss==0:
            if count == 1:
                character = 'x'
                index = int(input("\nplayer1 enter your index:"))
                stopGame = settingValue(index, character)
                count = -1

            else:
                count = 1
                character = 'o'
                index = int(input("\nplayer2 enter your index:"))
                stopGame = settingValue(index, character)

        #stopping loop and game by checking conditions
        if stopGame == 1:
            print("Game end")  #End of game
            # showing marked positions and final result
            print("Final marked positions")
            for i in range(3):
                for j in range(3):
                    print(gameArray[i][j], end="  ")
                print("")
            break

        #showing position and marked places
        print("")
        for i in range(3):
            for j in range(3):
                print(posArray[i][j],end="  ")
            print("")


        for i in range(3):
            for j in range(3):
                print(gameArray[i][j], end="  ")
            print("")

        print("")
    else:
        print("Nobody won.\nGame Drawn")
