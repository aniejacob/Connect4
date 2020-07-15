# Author: Aniebiet Jacob
# Date: 11/7/2018
# Description:
# This program is a 2 player game of connect 4




#Load saved game for user if their is a game already saved

def loadgame():

    fileName = input("Please enter the name of the file you wish to load from: ")
    myFile = open(fileName, "r")
    board1 = []
    board = []
    number = []
    columns = 0
    rows = 0

    for line in myFile:
        line = line.strip()
        index = line

    index = int(index)
    myFile.close


    myFile = open(fileName, "r")
#This for loop gets the player (index) from the function
# This for loop creates the new list for the loaded board
    for i in myFile:
        i = i.strip()
        i = i[:-1]
        i = i.split(":")
        board1.append(i)



    myFile.close()

    for i in range(len(board1)-2):
        board.append(board1[i])



#This for loop finds how many columns are in the board for a future gameplay function
    for i in range(len(board)):
        for j in range(len(board[i])):
            columns = j+1


#This for loop finds how many rows are in the board for a future gameplay function
    for i in range(len(board)):
        rows = i+1


#This for loop adds the number of columns to the board
    for i in range(columns):
        number.append("")
    board.append(number)



    return board, index, rows, columns











#This function saves the board that the user is playing by taking in a board and the index
def savegame(board, index):

    fileName = input("What would you like to save your game as?")

    fileName = open(fileName, "w")

    stringB = ""


#This for loop saves the current board as rows of strings
    for i in range(len(board)):
        for j in range(len(board[i])):
            stringB = stringB + board[i][j] + ":"
        fileName.write(stringB)
        fileName.write("\n")
        stringB = ""
    fileName.write(str(index))

    fileName.close()
    print("File saved")








#Create board size by asking user what the row number should be. both must be equal to AT LEAST 5

def boardrow():


    row = int(input("Please enter the desired number of rows for the board: "))

#This while loop makes sure that the user doesn't request a board row bigger than 5
    while row < 5:
        row = int(input("Invalid row number, please enter a number of at least 5 for the desired amount of rows for the board: "))







    return row

#Create board size by asking user what the column number should be. both must be equal to AT LEAST 5
def boardcolumn():

    column  = int(input("Please enter the desired number of columns for the board: "))


#This while loop makes sure that the user doesn't request a board column bigger than 5
    while column < 5:
        column = int(input("Invalid column number, please enter a number of at least 5 for the desired amount of columns for the board: "))
    return column






#This function will create the board by taking in the number of rows and columns the user requested
def boardsize(rows,columns):

    board1 = []
    board = []
    number = []


#This for loop will go through the number of rows and put in the number of columns requested by the user in each row
    for i in range(rows):
        board1 = []
        for j in range(columns):
           board1.append("_")
        board.append(board1)

    for i in range(columns):
        number.append("")

    board.append(number)

    return board





#This function takes in the board which is a list of lists and will create it into an actual board for the user to view
def makeboard(board):
    stringboard = ""

#This for loop creates the board by converting each space into a string and concatinating those strings together, creating a new line for each row
    for i in range(len(board)):
        for j in range(len(board[i])):
            stringboard = stringboard + board[i][j]

        print(stringboard)
        stringboard = ""

    return board





#This function takes in the board and checks for a winner for positive and negative diagonals, verticals and horizontials
def whowins(board):

    index = 0
    x_piece = 'X'
    o_piece = 'O'
    player = 0

#This for loop checks to see if there is a horizontial winner for X by iterating over every 'space' in a row, and if it finds one, adding one to the place keeper index. once index = 4 that means there are 4 X's meaning player 1 won
    for i in range(len(board)):
        index = 0
        for j in range(len(board[i])):
            if x_piece == board[i][j]:
                index = index + 1

                if index == 4:
                    player = 1
            else:
                index = 0


    index = 0
#This for loop checks for a horizontial winner for O  by iterating over every 'space' in a row, and if it finds one, adding one to the place keeper index. once index = 4 that means there are 4 O's meaning player 2 won
    for i in range(len(board)):
        index = 0
        for j in range(len(board[i])):
            if o_piece == board[i][j]:
                index = index + 1
                if index == 4:
                    player = 2
            else:
                index = 0



    index = 0
#This for loop checks for vertical wins for o by iterating over every 'space' in a column by checking one index in a column for every row, and if it finds one, adding one to the place keeper index. once index = 4 that means there are 4 O's meaning player 2 won

    for i in range(len(board)):
        index = 0
        for j in range(len(board[i])):
            for i in range(len(board)):
                if o_piece == board[i][j]:
                    index = index + 1
                    if index == 4:
                        player = 2
                else:
                    index = 0



    index = 0
#This loop checks for vertical wins for x by iterating over every 'space' in a column by checking one index in a column for every row, and if it finds one, ading one to the place keeper index. once index = 4 that means there are 4 X's meaning player 1 won
    for i in range(len(board)):
        index = 0
        for j in range(len(board[i])):
            for i in range(len(board)):
                if x_piece == board[i][j] and index !=100:
                    index = index + 1
                    if index == 4 or index ==100:
                        index = 100
                        player = 1
                else:
                    index = 0



#For loop that checks for wins in a negative diagonal for O by iterating over every 'space' in a column by checking and index in a column for every row, and if it finds one, adding one to the place keeper index. once index = 4 that means there are 4 O's meaning player 2 won
    index = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if o_piece == board[i][j] and index !=100:
                 index = index + 1
                 i = i+1

                 if index == 4 or index ==100:
                     index = 100
                     player = 2
            else:
                index = 0

#For loop that checks for wins in a negative diagonal for x  by iterating over every 'space' in a column by checking and index in a column for every row, and if it find's one, adding one to the place keeper index. once index = 4 that means there are 4 X's meaning player 1 won

    index = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if x_piece == board[i][j] and index !=100:
                 index = index + 1
                 i = i+1

                 if index == 4 or index ==100:
                     index = 100
                     player = 1
            else:
                index = 0


    index = 0

#For loop that checks for positive diagonal wins for x  by iterating over every 'space' in a column backwards by checking and index in a column for every row starting with the last row, and if it find's one, adding one to the place keeper index. once index = 4 that means there are 4 X's meaning player 1 won
    for i in range(len(board)):
        for j in range(len(board[i])):
            if x_piece == board[i][j] and index !=100:
                 index = index + 1
                 i = i-1

                 if index == 4 or index ==100:
                     index = 100
                     player = 1
            else:
                index = 0


    index = 0

#For loop that checks for positive diagonal wins for o  by iterating over every 'space' in a column backwards by checking and index in a column for every row starting with the last row, and if it find's one, adding one to the place keeper index. once index = 4 that means there are 4 O's meaning player 2 won

    for i in range(len(board)):
        for j in range(len(board[i])):
            if o_piece == board[i][j] and index !=100:
                 index = index + 1
                 i = i-1
                 if index == 4 or index ==100:
                     index = 100
                     player = 2
            else:
                index = 0



    return player







#Play game starting with player on, and moving on to player to after player one has gone. place pieces into board as well
def gameplay(board, row, columns, index):

    winner = 0
    initial = row-1
    draw = row*columns


#This loop checks to make sure that their has been no winner declared from the whowins function and to see that the board isn't fill by ensure that number of moves isn't equal to the number of spaces on the board
    while winner != 1 and winner != 2 and index!=draw:


#If statment that allows player 1 to go
        if index%2 == 0:
            print("It's player 1's turn!")
            x_piece =input("Please choose a column (1 to "+str(columns)+") to put your piece into or 's' to save: ")


#While loop that makes sure that the column the user chooses exists when the input isn't to save
            if  x_piece != 's':
                while int(x_piece)>columns or int(x_piece)<0:
                    x_piece =input("Please choose a column ( 1 to "+str(columns)+") to put your piece into or 's' to save: ")

            if x_piece != 's':
                x_piece = int(x_piece)


#While loop that checks to see if a space in the board is full and if it is it makes the board put the next piece on top of the board by changing the initial cow the piece can enter into if an X or O is already in that spot
                while  board[initial][x_piece-1] == 'X' or board[initial][x_piece-1] == 'O' and initial != -1:
                    initial = initial - 1


#If else that allows the player to put a piece into the board if the column isn't full, but if it is full asks the user for a new input
                if initial != -1:

                    board[initial][x_piece-1] = 'X'

                    initial = row-1
                    index = index + 1

                else:
                    print("This column is full! Choose a new column!")
                    initial = row-1


#If the user selects s the board will be saved using the savegame function
            elif x_piece == 's':
                savegame(board, index)




#Statement that will comence if it is player 2's turn since the place keeper will be odd
        elif index%2 == 1:

            print("It's player 2's turn!")
            o_piece = input("Please choose a column ( 1 to "+str(columns)+") to put your piece into or 's' to save: ")

#While loop that makes sure that the column the user chooses exists when the input isn't to save
            if  o_piece != 's':
                while int(o_piece)>columns or int(o_piece)<0:
                    o_piece =input("Please choose a column (1 to "+str(columns)+") to put your piece into or 's' to save: ")

            if o_piece != 's':
                o_piece = int(o_piece)

#While loop that checks to see if a space in the board is full and if it is it makes the board put the next piece on top of the board by changing the initial cow the piece can enter into if an X or O is already in that spot
                while  board[initial][o_piece-1] == 'X' or board[initial][o_piece-1] == 'O' and initial != -1:
                    initial = initial - 1


#If else that allows the player to put a piece into the board if the column isn't full, but if it is full asks the user for a new input
                if initial != -1:

                    board[initial][o_piece-1] = 'O'

                    initial = row-1
                    index = index + 1


                else:
                    print("This column is full! Choose a new column!")
                    initial = row-1

#If the user selects s the board will be saved using the savegame function
            elif o_piece == 's':
                savegame(board, index)


#This part of the function will read in the new board into both of these functions to make the new board and check if anyone has won yet
        board = makeboard(board)
        winner = whowins(board)

#This if statement checks if the number of turns(index) is equal to the total number of spaces in the game(draw) to see if the game is a tie if no one has won yet
    if index == draw:
        print("It is a draw!")

    else:
        print("Player ",winner," has won!")





#This is the main function that will execute all othe functions
def main():

    print("Welcome to Connect Four")
    print("This game is for two players")

    playagain = 'y'

    game0 = input("Would you like to load a game (y/n)? ")

#This loop will ensure that if the user puts in invalid input that the user will be prompted for a new input
    while game0!='y' and game0!='n':
        game0 = input("Would you like to load a game (y/n)? ")


#This statement will load an old game and continue playing it
    if game0 == 'y':
        board1, index, rows, columns  = loadgame()
        board = makeboard(board1)
        newboard = gameplay( board, rows, columns, index)

        playagain = input("Would you like to play again? (y/n): ")
        while playagain != 'y' and playagain !='n':
            playagain = input("Would you like to play again? (y/n): ")
#This while loop will go through playing the game, and as long as the player inputing 'y' saying that they want to play, it will continue playing the game.
    while playagain== 'y':
        index = 0
        rows = boardrow()
        columns = boardcolumn()
        print("")
        board1 = boardsize(rows,columns)
        board = makeboard(board1)
        newboard = gameplay( board, rows, columns, index)
        playagain = input("Would you like to play again? (y/n): ")
        while playagain != 'y' and playagain !='n':
            playagain = input("Would you like to play again? (y/n): ")

    print("Thank you for playing Connect Four")



main()
