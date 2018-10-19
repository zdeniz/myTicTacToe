def start_screen():
    choice = ''
    global x_player
    global o_player

    while not (choice == 'O' or choice == 'X'):
        if not choice == '':
            print("\nc'mon u can do this")
        choice = input('Firs Player Select X or O\n').upper()

    print(f'First player chose {choice}')

    if choice == 'X':
        x_player = 'First Player'
        o_player = 'Second Player'
    else:
        x_player = 'Second Player'
        o_player = 'First Player'
    return choice


def create_chart():
    box_number = 0
    num_column_pos = [2, 8, 14]
    num_row_pos = [1, 5, 9]
    chart = ''

    for row_cnt in range(0, 11):
        for column_cnt in range(0, 17):
            pixel = ''
            if row_cnt == 3 or row_cnt == 7:
                chart += '='
            elif column_cnt == 5 or column_cnt == 11:
                pixel = '|'
            elif (column_cnt in num_column_pos) and (row_cnt in num_row_pos):
                box_number += 1
                pixel = str(box_number)
            else:
                pixel = ' '
            chart += pixel
        chart += '\n'
    return chart


def put_to(box_no, chart=' ', symbol=' '):
    new_chart = []
    lst_chart = list(chart)
    x_symbol = list('*   *  *  *   *')
    o_symbol = list(' *** *   * *** ')

    row = int((box_no - 1) / 3) * 4
    column = ((box_no - 1) % 3) * 6

    added = 0
    deleted = 0

    for i in range(0, len(lst_chart)):
        b = column + row * 18

        if i == b or i == (b + 18) or i == (b + 36):
            deleted = 4
            for j in range(0, 5):
                if symbol == 'X':
                    new_chart.append(x_symbol[added])
                elif symbol == 'O':
                    new_chart.append(o_symbol[added])
                else:
                    print('HAHA, nice try')
                    exit()
                added += 1
        elif deleted > 0:
            deleted -= 1
        else:
            new_chart.append(lst_chart[i])
    return ''.join(new_chart)


def make_your_move_screen(chart, whos_turn):
    put = 0
    global select
    global turn
    global x_places
    global o_places

    if whos_turn == 'X':
        input_val = input(f'{x_player}, Enter a number to put X: ')
        if input_val.isdigit() and not input_val == 0:
            put = int(input_val)
        elif input_val == 0:
            print('There is no 0 in chart...')
            return game_chart
        else:
            print('Pufff... Write a digit!')
            return game_chart

    elif whos_turn == 'O':
        input_val = input(f'{o_player}, Enter a number to put O: ')
        if input_val.isdigit() and not input_val == 0:
            put = int(input_val)
        elif input_val == 0:
            print('There is no 0 in chart...')
            return game_chart
        else:
            print('Pufff... Write a digit!')
            return game_chart

    if not (put in select):
        select.append(put)
        ret_val = put_to(put, chart, whos_turn)

        if turn == 'X':
            x_places.append(put)
            turn = 'O'
        elif turn == 'O':
            o_places.append(put)
            turn = 'X'
        return ret_val

    else:
        print('Area occupied try some where else !')
        return game_chart


def check_game_status(game_chart):
    global select
    global end_game
    global x_places
    global o_places

    tie_end = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ends = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in range(8):
        if set(ends[i]) <= set(x_places):
            print('\n' + game_chart)
            print('X Wins!')
            print('game over!')
            end_game = True
            return
        elif set(ends[i]) <= set(o_places):
            print('\n' + game_chart)
            print('O Wins!')
            print('game over!')
            end_game = True
            return
        
    if set(tie_end) == set(select):
        print('\n' + game_chart)
        print('Its A Tie!')
        print('game over!')
        end_game = True
        return


select = []
x_places = []
o_places = []
end_game = False
turn = start_screen()
game_chart = create_chart()

while not end_game:
    print('\n' + game_chart)
    game_chart = make_your_move_screen(game_chart, turn)
    check_game_status(game_chart)
exit()

#y = put_to(1, z, 'X')
#y = put_to(2, y, 'O')
#y = put_to(3, y, 'X')
#print(y)

# print('*   *| *** |     ')
# print('  *  |*   *|  3  ')
# print('*   *| *** |     ')
# print('=================')
# print('     |     |     ')
# print('  4  |  5  |  6  ')
# print('     |     |     ')
# print('=================')
# print('     |     |     ')
# print('  7  |  8  |  9  ')
# print('     |     |     ')

# print('     |     |     ')
# print('  1  |  2  |  3  ')
# print('     |     |     ')
# print('=================')
# print('     |     |     ')
# print('  4  |  5  |  6  ')
# print('     |     |     ')
# print('=================')
# print('     |     |     ')
# print('  7  |  8  |  9  ')
# print('     |     |     ')
