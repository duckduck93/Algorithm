import pprint
import sys
from collections import deque

CHECK = 9


def count(piece):
    answer = 0
    for c in piece:
        if c == '1':
            answer += 1
    return answer


def match(piece1, piece2):
    height1 = len(piece1)
    height2 = len(piece2)
    if height1 != height2:
        return False
    width1 = len(piece1[0])
    width2 = len(piece2[0])
    if width1 != width2:
        return False

    for y in range(height1):
        for x in range(width1):
            if piece1[y][x] != piece2[y][x]:
                return False

    return True


def rotate(piece):
    height = len(piece)
    width = len(piece[0])

    board = [[0 for _ in range(height)] for _ in range(width)]
    for y in range(height):
        for x in range(width):
            if piece[y][x] == 0:
                continue
            board[x][height - y - 1] = 1
    return board


def make_piece(piece_coordinate):
    min_y, min_x = sys.maxsize, sys.maxsize
    max_y, max_x = -1, -1
    for co in piece_coordinate:
        y, x = co
        min_y, min_x = min(min_y, y), min(min_x, x)
        max_y, max_x = max(max_y, y), max(max_x, x)

    height = max_y - min_y
    width = max_x - min_x
    board = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for co in piece_coordinate:
        _y, _x = co
        y, x = _y - min_y, _x - min_x
        board[y][x] = 1
    return board


def find_coordinates(_y, _x, board, find_blank: bool):
    width = len(board)

    q = deque()
    board[_y][_x] = CHECK
    q.append((_y, _x))
    piece_coordinate = [(_y, _x)]

    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if y + dy < 0 or x + dx < 0:
                continue
            if y + dy >= width or x + dx >= width:
                continue

            ny, nx = y + dy, x + dx
            if board[ny][nx] == CHECK:
                continue
            if board[ny][nx] == (1 if find_blank else 0):
                continue
            board[ny][nx] = CHECK
            q.append((ny, nx))
            piece_coordinate.append((ny, nx))

    return piece_coordinate


def find_piece(_y, _x, board, find_blank: bool):
    coordinates = find_coordinates(_y, _x, board, find_blank)
    return make_piece(coordinates)


def solution(game_board, table):
    width = len(game_board)

    blank_pieces = []
    fill_pieces = set()
    for y in range(width):
        for x in range(width):
            if game_board[y][x] == CHECK:
                continue
            if game_board[y][x] == 1:
                continue
            piece = find_piece(y, x, game_board, True)
            rows = list(map(lambda arg: ''.join(map(lambda i: str(i), arg)), piece))
            blank_pieces.append(','.join(rows))

    index = 0
    for y in range(width):
        for x in range(width):
            if table[y][x] == CHECK:
                continue
            if table[y][x] == 0:
                continue

            piece = find_piece(y, x, table, False)
            rotate90 = rotate(piece)
            rotate180 = rotate(rotate90)
            rotate270 = rotate(rotate180)

            fill_pieces.add(
                (index, ','.join(list(map(lambda arg: ''.join(map(lambda i: str(i), arg)), piece))))
            )
            fill_pieces.add(
                (index,','.join(list(map(lambda arg: ''.join(map(lambda i: str(i), arg)), rotate90))))
            )
            fill_pieces.add(
                (index,','.join(list(map(lambda arg: ''.join(map(lambda i: str(i), arg)), rotate180))))
            )
            fill_pieces.add(
                (index,','.join(list(map(lambda arg: ''.join(map(lambda i: str(i), arg)), rotate270))))
            )
            index += 1

    pprint.pprint(blank_pieces)
    pprint.pprint(fill_pieces)
    used_pieces = [False] * index
    answer = 0
    for piece in blank_pieces:
        for index, puzzle in fill_pieces:
            if used_pieces[index]:
                continue
            if piece == puzzle:
                answer += count(piece)
                used_pieces[index] = True
                break

    return answer


if __name__ == '__main__':
    print(solution(
        [[1, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 1],
         [1, 1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0]],

        [[1, 0, 0, 1, 1, 0],
         [1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 1, 1],
         [0, 0, 1, 0, 0, 0],
         [1, 1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 0]]))
    print(solution(
        [[0, 0, 0],
         [1, 1, 0],
         [1, 1, 1]],

        [[1, 1, 1],
         [1, 0, 0],
         [0, 0, 0]]))
