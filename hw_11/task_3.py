def draw_square(side_length, symbol, filled):
    for i in range(side_length):
        for j in range(side_length):
            if filled or (i == 0 or i == side_length - 1 or j == 0 or j == side_length - 1):
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print() #  закриваємо функ


side_length = 5
symbol = '*'
filled = True

draw_square(side_length, symbol, filled)
