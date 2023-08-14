# board = [' ', 'O', 'X',
#          ' ', 'X', 'O',
#          'O', 'X', ' ']

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']


def possible_moves(s):
    return [i for i, value in enumerate(s) if value == ' ']


def check_terminal(s, letter):
    # For Row
    for k in range(3):
        if all([i == letter for i in s[(k*3):3*(k+1)]]):
            return True

    # For Col
    for k in range(3):
        if all([i == letter for i in [s[k], s[k+3], s[k+6]]]):
            return True

    # For Diagonal
    if all([s[0] == letter, s[4] == letter, s[8] == letter]):
        return True
    if all([s[2] == letter, s[4] == letter, s[6] == letter]):
        return True


def num_empty_squares(s):
    return s.count(' ')


def print_board(s, player):
    print(f'{player} Turn')
    for row in range(3):
        print(s[row*3:row*3+3])
    print('---------------')


def minimax(s, player):
    if num_empty_squares(s) == 0:
        return 0
    if check_terminal(s, 'X'):
        return 1
    if check_terminal(s, 'O'):
        return -1

    if player == 'X':
        best_score = -2
        for move in possible_moves(s):
            s[move] = player
            best_score = max(best_score, minimax(s, 'O'))
            s[move] = ' '
        return best_score

    if player == 'O':
        best_score = 2
        for move in possible_moves(s):
            s[move] = player
            best_score = min(best_score, minimax(s, 'X'))
            s[move] = ' '

        return best_score


def best_move(player):
    if player == 'X':
        # print_board(board, 'X')
        best_score = -2
        output_move = None
        for move in possible_moves(board):
            board[move] = 'X'
            score = minimax(board, 'O')
            # print(move, score)
            if score > best_score:
                best_score = score
                output_move = move
            board[move] = ' '
        return output_move
        # print(best_score, best_move, 'aaaaaaaaaaaaaaaa')

    if player == 'O':
        # print_board(board, 'O')
        best_score = 2
        output_move = None
        for move in possible_moves(board):
            board[move] = 'O'
            score = minimax(board, 'X')
            if score < best_score:
                best_score = score
                output_move = move
            board[move] = ' '
        return output_move
        # print(best_score, best_move, 'aaaaaaaaaaaaaaaa')


def user_input():
    print('Positions:')
    for i in range(3):
        print(f'{i*3} | {i*3+1} | {i*3+2}')
    return input('Choose Position: ')


def game():
    # # Computer Vs. Computer
    # player_turn = 'X'
    # while True:
    #     if player_turn == 'X':
    #         player_turn = 'O'
    #     else:
    #         player_turn = 'X'
    #
    #     board[best_move(player_turn)] = player_turn
    #     print_board(board, player_turn)
    #     if num_empty_squares(board) == 0:
    #         print('Tie!')
    #         return 'Tie'
    #     if check_terminal(board, player_turn):
    #         print(f'{player_turn} Won!')
    #         return player_turn

    # Computer Vs. Human
    player_turn = 'O'
    while True:
        if player_turn == 'X':
            user_pos = user_input()
            while int(user_pos) < 0 or int(user_pos) > 8 or board[int(user_pos)] != ' ':
                print('You Chose Invalid Position')
                print_board(board, player_turn)
                user_pos = user_input()
            board[int(user_pos)] = player_turn
            if num_empty_squares(board) == 0:
                print_board(board, player_turn)
                print('Tie!')
                return
            if check_terminal(board, player_turn):
                print_board(board, player_turn)
                print(f'{player_turn} Won!')
                return
            print_board(board, player_turn)
            player_turn = 'O'
        else:
            board[best_move(player_turn)] = player_turn
            if num_empty_squares(board) == 0:
                print_board(board, player_turn)
                print('Tie!')
                return
            if check_terminal(board, player_turn):
                print_board(board, player_turn)
                print(f'{player_turn} Won!')
                return
            print_board(board, player_turn)
            player_turn = 'X'


print_board(board, 'None')
game()
# who_won = {'X': 0, 'O': 0, 'Tie': 0}
# for _ in range(10):
#     board = [' ', ' ', ' ',
#              ' ', ' ', ' ',
#              ' ', ' ', ' ']
#     value = game()
#     if value == 'X':
#         who_won['X'] += 1
#     if value == 'O':
#         who_won['O'] += 1
#     if value == 'Tie':
#         who_won['Tie'] += 1
#
# print(who_won)
