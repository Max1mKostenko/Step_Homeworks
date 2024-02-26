import random


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


def generate_board():
    nums = list(range(1, 16))
    random.shuffle(nums)
    board = [nums[i:i + 4] for i in range(0, 16, 4)]
    board[3][3] = " "
    return board


def find_empty_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == " ":
                return i, j


def is_valid_move(move):
    return move in ["w", "a", "s", "d"]


def move_tile(board, move):
    empty_row, empty_col = find_empty_position(board)
    if move == "w" and empty_row < 3:
        board[empty_row][empty_col], board[empty_row + 1][empty_col] = board[empty_row + 1][empty_col], \
        board[empty_row][empty_col]
    elif move == "a" and empty_col < 3:
        board[empty_row][empty_col], board[empty_row][empty_col + 1] = board[empty_row][empty_col + 1], \
        board[empty_row][empty_col]
    elif move == "s" and empty_row > 0:
        board[empty_row][empty_col], board[empty_row - 1][empty_col] = board[empty_row - 1][empty_col], \
        board[empty_row][empty_col]
    elif move == "d" and empty_col > 0:
        board[empty_row][empty_col], board[empty_row][empty_col - 1] = board[empty_row][empty_col - 1], \
        board[empty_row][empty_col]


def is_solved(board):
    return all(board[i][j] == i * 4 + j + 1 for i in range(4) for j in range(4)) and board[3][3] == " "


def play_game():
    board = generate_board()
    print("Добро пожаловать в игру 'Пятнашки'!\n")
    print("Используйте клавиши WASD для перемещения плиток, чтобы упорядочить их.\n")
    print_board(board)
    moves = 0

    while not is_solved(board):
        move = input("Введите направление перемещения (WASD): ").lower()
        if is_valid_move(move):
            move_tile(board, move)
            moves += 1
            print_board(board)
        else:
            print("Неверный ввод. Используйте клавиши WASD.")

    print(f"Поздравляем! Вы решили головоломку за {moves} ходов.")


if __name__ == "__main__":
    play_game()
