#!/usr/bin/env python
# coding: utf-8

# In[3]:


board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}

player = 1
total_moves = 0
end_check = 0


def check():
    for mark, name in zip(('X', 'O'), ('One', 'Two')):
        # horizontal
        for col in 'TMD':
            if all(board['{}{}'.format(col, num)] == mark for num in range(1, 4)):
                print('Player {} Won!!'.format(name))
                return 1

        # vertical
        for row in range(1, 4):
            if all(board['{}{}'.format(col, row)] == mark for col in 'TMD'):
                print('Player {} Won!!'.format(name))
                return 1

        # diagonal
        if all(board['{}{}'.format(col, row)] == mark for col, row in zip('TMD', range(1, 4))) or \
                all(board['{}{}'.format(col, row)] == mark for col, row in zip('TMD', range(3, 0, -1))):
            print('Player {} Won!!'.format(name))
            return 1
    return 0


print(('T1|T2|T3\n'
       '- +- +-\n'
       'M1|M2|M3\n'
       '- +- +-\n'
       'D1|D2|D3\n'
       '*********'))

while True:
    print('{}|{}|{}'.format(board['T1'], board['T2'], board['T3']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['M1'], board['M2'], board['M3']))
    print('-+-+-')
    print('{}|{}|{}'.format(board['D1'], board['D2'], board['D3']))

    end_check = check()

    if total_moves == 9 or end_check == 1:
        break

    while True:
        p_input = input('player {}: '.format('one' if player == 1 else 'two'))
        if p_input.upper() in board and board[p_input.upper()] == ' ':
            board[p_input.upper()] = 'X' if player == 1 else 'O'
            player = 2
            break

        else:
            print('Invalid input, please try again')
            continue
    total_moves += 1
    print('*********\n')
