""" Tic Tac Toe Game """

# Globals

players = {'x': [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]],'o': [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]}
print(players['x'])
gameList = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
winnerPossibilities = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Functions

def getIndex():
# gets the user input and returns it with validations

    index = input('What position do you want to choose? (1-9):\n')

    while True:
        if index.isdigit() and int(index) in range(1,10):
            return int(index)
            break
        print('Please type a valid input!')
        index = input('What position do you want to choose? (1-9)')
        
def updateList(player, index):
# Check if the input of the user is valid and update the player list as well as the game list, returns boolean

    row, excess = [0,1] if index in range(1,4) else [1,4] if index in range(4,7) else [2,7]

    if gameList[row][index-excess] == ' ':
        players[player][row][index-excess] = index -1
        gameList[row][index-excess] = player 
        return True

    return False

def isWinner(player):
# checks if the player won the game, returns a boolean
    column = [
        [players[player][0][0], players[player][1][0], players[player][2][0]], 
        [players[player][0][1], players[player][1][1], players[player][2][1]], 
        [players[player][0][2], players[player][1][2], players[player][2][2]]
        ]
    row = [item for item in players[player]]
    diagonal = [
        [players[player][0][0], players[player][1][1], players[player][2][2]],
        [players[player][0][2], players[player][1][1], players[player][2][0]]
        ]
    playerCombinations = column + row + diagonal
    for item in playerCombinations:
        if item in winnerPossibilities:
            return True

    return False

def isTie():
# checks if the game is tied, returns boolean
    
    for row in gameList:
        for item in row:
            if item == ' ':
                return False
    
    return True 

def printGame():
# prints the game board
    print(f" {gameList[0][0]} | {gameList[0][1]} | {gameList[0][2]} \n------------\n {gameList[1][0]} | {gameList[1][1]} | {gameList[1][2]} \n------------\n {gameList[2][0]} | {gameList[2][1]} | {gameList[2][2]} \n\n")

# Game

def game():
# tic tac toe game logic
    
    # Introducction

    print("\n\nTIC TAC TOE \n\nWelcome, let's have some fun!\n\nGame positions:\n\n")
    print(" 1 | 2 | 3 \n------------\n 4 | 5 | 6 \n------------\n 7 | 8 | 9 \n\n")
    print("The 'x' player starts!\n\n")

    player = None
    changer = True 
    index = None

    while(True):
        player = 'x' if changer else 'o'
        
        print(f'\n\n\n{player} Turn!\n\n')
        printGame()
        index = getIndex()
        if not updateList(player, index):
            print("\n\n\nSorry, that's not a valid position!")
            continue
        

        if isWinner(player):
            print(f'CONGRATULATIONS {player}!!!\nYou have won!')
            break
        elif isTie():
            print(f"\n\n\nWOW!!!\nIt's a tie!")
            break
        else:
            changer = not changer
            print(players)

# Runs the game
game()