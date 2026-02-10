TheBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
BoardKeys = []
for key in TheBoard:
    BoardKeys.append(key)
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(TheBoard)
        print("It's your turn, " + turn + ". Move to which place?")
        move = input()
        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count += 1
        else:
            print("That place is already filled. Move to another place?")
            continue
        if count >= 5: 
            if TheBoard['1'] == TheBoard['2'] == TheBoard['3'] != ' ': #across the top
                printBoard(TheBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif TheBoard['4'] == TheBoard['5'] == TheBoard['6'] != ' ': #across the middle
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            #VERTICAL WIN CHECKS
            elif TheBoard['7'] == TheBoard['8'] == TheBoard['9'] != ' ': #along the bottom
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif TheBoard['1'] == TheBoard['4'] == TheBoard['7'] != ' ': #down the left side
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif TheBoard['2'] == TheBoard['5'] == TheBoard['8'] != ' ': #down the middle
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif TheBoard['3'] == TheBoard['6'] == TheBoard['9'] != ' ': #down the right side
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard['9'] != ' ': #diagonal
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif TheBoard['3'] == TheBoard['5'] == TheBoard['7'] != ' ': #diagonal
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            break
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do want to play Again? (y/n)\n")
    if restart == "y" or restart == "Y":
        for key in BoardKeys:
            TheBoard[key] = " "
        game()
if __name__ == "__main__":
    game()