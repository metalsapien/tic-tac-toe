
########################################
########################################
######        Tic-Tac-Toe       ########
########################################
######   Author: Harsh Nath Jha   ######
########################################
########################################

import random
from IPython.display import clear_output
#Note: IPython.display is exclusive for iPython Notebook environments!

print('Welcome to Tic-Tac-Toe!')

#GAME PLAY

while True:
    new_board = [' ']*10
    player1 = ''
    ready = True

   #Player chooses a Symbol out of 'X' and 'O'

    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1 Choose X or O: ")
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    print("You chose {}, Player 2 chose {}".format(player1,player2))

    #Determining which player goes first

    turn = random.randint(1,2)
    print("Player {} will go first".format(turn))

    begin = input("Are you ready to begin? (Yes/No): ")
    
    if begin.upper() == 'NO':
        ready = False
     
    def display_board(board):
        ''' Displaying the game-board '''
        clear_output()
        #Note: IPython.display is exclusive for iPython Notebook environments!
        print('##############################\n####    Tic -Tac - Toe    ####\n##############################\n')
        print('           ||   ||\n'+'         '+board[1]+' || '+board[2]+' || '+board[3]+'\n           ||   ||')
        print('       ===============\n           ||   ||')
        print('        '+board[4]+'  || '+board[5]+' || '+board[6]+'\n           ||   ||')
        print('       ===============\n           ||   ||')
        print('        '+board[7]+'  || '+board[8]+' || '+board[9]+'\n           ||   ||')
           
    def player_choice(board):
        ''' Taking the mark-position as input from the user '''
        position = 0
        while position not in range(1,10) or not space_check(board,position):
            position = int(input('Enter your choice (1-9): '))
        return position

    def placemarker(board, player_mark, position):
        ''' Placing X and O marks in the game-board '''
        board[position] = player_mark
        
    def win_check(board, mark):
        ''' To determine the winner by matching all the winning patters '''
        return((board[1] == board[2] == board[3] == mark)
           or (board[4] == board[5] == board[6] == mark)
           or (board[7] == board[8] == board[9] == mark)
           or (board[1] == board[4] == board[7] == mark)
           or (board[1] == board[5] == board[9] == mark)
           or (board[2] == board[5] == board[8] == mark)
           or (board[3] == board[5] == board[7] == mark)
           or (board[3] == board[6] == board[9] == mark))

 	def space_check(board, position):
        ''' Checking whether a position is already occupied '''
        return board[position] == ' '
    
    def full_board_check(board):
        ''' Checking whether all the positions have been taken on the game-board '''
        draw = True
        for i in range(1,10):
            if space_check(board,i):
                draw = False
        return draw
               
    #To check 

    def replay():
        '''  Replay the game '''
        again = input("Type 'Yes' to play again, 'No' to quit: ")
        if again.upper() == 'YES':
            ready = True
        return again.upper() == 'YES'
            
 #Game-play begins:

    while ready:
        #Player 1's turn:
        if turn == '1':

            display_board(new_board)
            position = player_choice(new_board)
            placemarker(new_board,player1,position)
            
            #Checking if Player 1 has won!

            if win_check(new_board,player1):
                display_board(new_board)
                print('\nCongratulations! You have won!')
                break

            #Whether it's a draw! 

            elif full_board_check(new_board):
                display_board(new_board)
                print('\nThe game is a draw!')
                break
            
            #Once Player 1's mark is placed and Win/Draw is examined, Players switch their turns

            else:
                turn = '2'
            
        #Player 2's turn:
        else:
            display_board(new_board)
            position = player_choice(new_board)
            placemarker(new_board,player2,position)
            
            #Checking if Player 1 has won!

            if win_check(new_board,player2):
                display_board(new_board)
                print('\nPlayer 2 has won!')
                break
                
            #Whether it's a draw!

            elif full_board_check(new_board):
                display_board(new_board)
                print('\nThe game is a draw!')
                break
            
            #Once Player 2's mark is placed and Win/Draw is examined, Players switch their turns

            else:
                turn = '1'
  
    if not replay():
        break

#The game ends here if the user inputs 'No' and its replayed if a 'Yes' input is detected
