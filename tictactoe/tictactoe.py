game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
choose = list()
print(f'''tictactoe''')
print(f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| {"".join(map(str, game))[6:9]} |')
print('__________')
x = 'X'
o = '0'
x_win = 0
o_win = 0
buf = x
pop = 0
coordinates = 0


def Restart():
    global choose
    restart = input('''do u want to play again?
    1 - restart
    2 - exit''')

    if restart.isnumeric():
        restart = int(restart)
        if restart == 1:
            choose.clear()
            play()
        elif restart == 2:
            print('Bye')
        else:
            print('try again')
            Restart()
    else:
        print('try again')
        Restart()


def play():
    global game
    game = list(['_', '_', '_', '_', '_', '_', '_', '_', '_'])
    global x, o, x_win, o_win, pop, buf, coordinates
    while True:
        pop = 0
        coordinates = 0
        word = "".join(map(str, game))
        if game[0] == 'X' and game[1] == 'X' and game[2] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[0] == 'X' and game[3] == 'X' and game[6] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[0] == 'X' and game[4] == 'X' and game[8] == 'X':
            print('X WON')
            x_win = 1
        elif game[2] == 'X' and game[5] == 'X' and game[8] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[2] == 'X' and game[4] == 'X' and game[6] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[6] == 'X' and game[7] == 'X' and game[8] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[1] == 'X' and game[4] == 'X' and game[7] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[3] == 'X' and game[4] == 'X' and game[5] == 'X':
            print('X WON')
            x_win = 1
            break
        elif game[0] == 'O' and game[1] == 'O' and game[2] == '0':
            print('0 WON')
            o_win = 1
            break
        elif game[0] == 'O' and game[3] == 'O' and game[6] == 'O':
            print('O WON')
            o_win = 1
            break
        elif game[0] == 'O' and game[4] == 'O' and game[8] == 'O':
            print('O WON')
            o_win = 1
        elif game[2] == 'O' and game[5] == 'O' and game[8] == 'O':
            print('O WON')
            o_win = 1
            break
        elif game[2] == 'O' and game[4] == 'O' and game[6] == 'O':
            print('O WON')
            o_win = 1
            break
        elif game[6] == 'O' and game[7] == 'O' and game[8] == 'O':
            print('O WON')
            o_win = 1
            break
        elif game[1] == 'O' and game[4] == 'O' and game[7] == 'O':
            print('O WON')
            o_win = 1
            break
        elif game[3] == 'O' and game[4] == 'O' and game[5] == 'O':
            print('O WON')
            o_win = 1
            break
        elif '_' not in game and x_win == 0 and o_win == 0:
            print('tie')
            break
        print(f'Choose cells: {word}')
        player = str(input(f'enter {buf}\nCoordinates:>>> '))
        split_player = ''.join(player.split())
        coordinates = {'1 1': 0, '1 2': 1, '1 3': 2, '2 1': 3, '2 2': 4, '2 3': 5, '3 1': 6, '3 2': 7, '3 3': 8}
        numbers = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
        if player.isnumeric():
            print('pls, enter true coordinates')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        elif str(player) not in str(numbers) and player != player.isnumeric():
            print('coordinates must be from 1 to 3!')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        elif split_player.isnumeric():
            pop = coordinates[player]
        else:
            print('U must enter numbers!')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue

        if pop < 0 or pop > 8:
            print('Unknown')
            continue
        elif pop in choose:
            print('This cell is occupied! Choose another one!')
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            continue
        else:
            choose.append(pop)
            game.pop(pop)
            game.insert(pop, buf)
            print('__________')
            print(
                f'| {"".join(map(str, game))[0:3]} |\n| {"".join(map(str, game))[3:6]} |\n| \
{"".join(map(str, game))[6:9]} |')
            print('__________')
            if buf == x:
                buf = o
            elif buf == o:
                buf = x
    x_win = 0
    o_win = 0
    buf = x
    Restart()


play()
