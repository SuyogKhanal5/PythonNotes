from IPython.display import clear_output

blank_board = [' ']*10    

def display_board(board):
    print(board[7] + '|' + board[8] + '|'+ board[9])
    print(board[4] + '|' + board[5] + '|'+ board[6])
    print(board[1] + '|' + board[2] + '|'+ board[3])

display_board(blank_board)

def player_input():
    
    marker = ''
    
    while marker != "X" and marker != "O":
         marker = input('Player One, Choose X or O:')
       
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 = 'X'
        
    print(player1,player2)
    
move = ''

while move != 1-9:
    move = input('Where would you like to place your marker? (Look at the NumPad to see which number places where)')
