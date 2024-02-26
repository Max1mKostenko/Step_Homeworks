def is_valid_move(board, move, visited):
    x, y = move
    if 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == 0 and (x, y) not in visited:
        return True
    return False


def get_legal_moves(board, x, y, visited):
    moves = [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2),
             (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)]
    legal_moves = [move for move in moves if is_valid_move(board, move, visited)]
    return legal_moves


def knight_tour(board, x, y, move_number, visited):
    board[x][y] = move_number
    visited.add((x, y))

    if move_number == len(board) * len(board[0]):
        return True

    legal_moves = get_legal_moves(board, x, y, visited)
    for next_x, next_y in sorted(legal_moves, key=lambda move: len(get_legal_moves(board, move[0], move[1], visited))):
        if knight_tour(board, next_x, next_y, move_number + 1, visited):
            return True

    board[x][y] = 0
    visited.remove((x, y))
    return False


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))


def main():
    board_size = 8
    board = [[0] * board_size for _ in range(board_size)]
    start_x = int(input("Введите начальную координату по горизонтали (от 0 до 7): "))
    start_y = int(input("Введите начальную координату по вертикали (от 0 до 7): "))

    if knight_tour(board, start_x, start_y, 1, set([(start_x, start_y)])):
        print("Маршрут коня:")
        print_board(board)
    else:
        print("Маршрут не найден.")


if __name__ == "__main__":
    main()
