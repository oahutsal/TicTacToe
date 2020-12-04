import random
chanses = list('123456789')
board = list('''
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|

''')
n = False
#indexes = []
#for i in board:
#    if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
#        indexes.append(board.index(i))
#print(indexes)
#indexes = [44, 50, 56, 124, 130, 56, 204, 210, 216]

def xo_func():
    print('\nWelcome to the tic tac toe!')
    player_choise = input('Choose the X or O: ').upper()
    if player_choise == 'X':
        computer_choise = 'O'
    elif player_choise == 'O':
        computer_choise = 'X'
    else: 
        print('Error 404. You write wrong symbol!')
        return False
    print('You are the ' + player_choise + ', computer is ' + computer_choise)
    return player_choise, computer_choise

player_choise = xo_func()
#player_choise[0] is player, player_choise[1] is computer

def place_func():
    player_place = input('Write the nummer (1-9) to mark this place: ')
    if player_place in chanses:
        random_num = str(random.choice(chanses))
        board.insert(board.index(player_place), player_choise[0])
        board.remove(player_place)
        board.insert(board.index(random_num), player_choise[1])
        board.remove(random_num)
        chanses.remove(player_place)
        chanses.remove(random_num)
        print(''.join(board))
        print(str(chanses))
        return True
    elif len(chanses) == 0:
        a = input('Game over!\nDo you want to continue?[y/n]')
        return a.upper()
    else: 
        print('ERROR!!!\nOn ly numbers which are free!\nYOU LOSE!')
        return False

def combinations_player():
    if board[204] and board[210] and board[216] == player_choise[0]:
        return True
    elif board[124] and board[130] and board[136] == player_choise[0]:
        return True
    elif board[44] and board[50] and board[56] == player_choise[0]:
        return True
    elif board[204] and board[124] and board[44] == player_choise[0]:
        return True
    elif board[210] and board[130] and board[50] == player_choise[0]:
        return True
    elif board[136] and board[56] and board[216] == player_choise[0]:
        return True
    elif board[204] and board[130] and board[56] == player_choise[0]:
        return True
    elif board[44] and board[130] and board[216] == player_choise[0]:
        return True
    else: return False

def combinations_computer():
    if board[204] and board[210] and board[216] == player_choise[1]:
        return True
    elif board[124] and board[130] and board[136] == player_choise[1]:
        return True
    elif board[44] and board[50] and board[56] == player_choise[1]:
        return True
    elif board[204] and board[124] and board[44] == player_choise[1]:
        return True
    elif board[210] and board[130] and board[50] == player_choise[1]:
        return True
    elif board[136] and board[56] and board[216] == player_choise[1]:
        return True
    elif board[204] and board[130] and board[56] == player_choise[1]:
        return True
    elif board[44] and board[130] and board[216] == player_choise[1]:
        return True
    else: return False


while not n:
    place = place_func()
    comb_comp = combinations_computer()
    player_comb = combinations_player()
    if place == True:
        continue
    elif place == False:
        break
    elif place == 'Y':
        chanses = list('123456789')
        board = list('''
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|

        ''')
        continue
    elif place == "N":
        break
    if comb_comp == True:
        print('Player ' + player_choise[1] + ' win!')
        break
    elif comb_comp == False:
        continue
    if player_comb == True:
        print('Player ' + player_choise[0] + ' win!')
        break
    elif player_comb == False:
        continue
    
