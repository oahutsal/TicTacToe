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
#indexes = [44, 50, 56, 124, 130, 136, 204, 210, 216]

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
print(''.join(board))
#player_choise[0] is player, player_choise[1] is computer
def place_func():
    player_place = input('Write the nummer (1-9) to mark this place: ')
    if player_place in chanses:
        if len(chanses) != 0:
            if player_place in chanses:
                board.insert(board.index(player_place), player_choise[0])
                board.remove(player_place)
                chanses.remove(player_place)
                if len(chanses) > 0:
                    random_num = str(random.choice(chanses))
                    board.insert(board.index(random_num), player_choise[1])
                    board.remove(random_num)
                    chanses.remove(random_num)
                elif len(chanses) == 0:
                    return False
            print(''.join(board))
            print(str(chanses))
    else: 
        print('ERROR!!!\nOnly numbers which are free!\n' + str(chanses))

def combinations_player():
    if board[204] + board[210] + board[216] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[124] + board[130] + board[136] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[44] + board[50] + board[56] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[204] + board[124] + board[44] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[210] + board[130] + board[50] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[136] + board[56] + board[216] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[204] + board[130] + board[56] == player_choise[0] * 3:
        return player_choise[0] * 3
    elif board[44] + board[130] + board[216] == player_choise[0] * 3:
        return player_choise[0] * 3

def combinations_computer():
    if board[204] + board[210] + board[216] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[124] + board[130] + board[136] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[44] + board[50] + board[56] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[204] + board[124] + board[44] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[210] + board[130] + board[50] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[136] + board[56] + board[216] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[204] + board[130] + board[56] == player_choise[1] * 3:
        return player_choise[1] * 3
    elif board[44] + board[130] + board[216] == player_choise[1] * 3:
        return player_choise[1] * 3

while not n:
    place = place_func()
    if place != False:
        computer_comb = combinations_computer()
        player_comb = combinations_player()
        if player_comb == player_choise[0] * 3:
            print('Player ' + player_choise[0] + ' win!')
            a = input('GAME OVER! Do you want to continue?[y/n] ')
            if a.lower == 'y':
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
            elif a.lower() == 'n':
                break
            else:
                break
        elif computer_comb == player_choise[1] * 3:
            print('Player ' + player_choise[1] + ' win!')
            a = input('GAME OVER! Do you want to continue?[y/n] ')
            if a.lower() == 'y':
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
            elif a.lower() == 'n':
                break
            else:
                break
        else:
            continue
    elif place == False:
        a = input('GAME OVER! Do you want to continue?[y/n] ')
        if a.lower() == 'y':
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
        elif a.lower() == 'n':
            break
    
