import pprint
from collections import defaultdict


def find_coordinate(block_cells):
    left_bottom_y = max(map(lambda arg: arg[0], block_cells))
    left_bottom_x = min(map(lambda arg: arg[1], block_cells))

    right_top_y = min(map(lambda arg: arg[0], block_cells))
    right_top_x = max(map(lambda arg: arg[1], block_cells))
    return [(left_bottom_y, left_bottom_x), (right_top_y, right_top_x)]


def find_block(board):
    blocks = defaultdict(lambda: {'coordinate': [], 'cells': []})
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != 0:
                blocks[board[y][x]]['cells'].append((y, x))

    for num in blocks:
        blocks[num]['coordinate'] = find_coordinate(blocks[num]['cells'])
    return dict(blocks)


# todo find_unavailable 로 만들어서 찾기
def find_available(board, sta_x, end_x):
    height = len(board)
    width = len(board[0])

    for x in range(sta_x, end_x):
        for y in range(height):
            if board[y][x] == 0 and y + 1 == height:
                board[y][x] = -1
                break
            if board[y][x] == 0 and board[y + 1][x] == 0:
                board[y][x] == -1
                continue
            if board[y][x] == 0 and board[y + 1][x] != 0:
                board[y][x] = -1
                break


def is_rectangle(board, num, block):
    left_bottom, right_top = block['coordinate']
    for y in range(right_top[0], left_bottom[0] + 1):
        for x in range(left_bottom[1], right_top[1] + 1):
            if board[y][x] != num and board[y][x] != -1:
                return False
    return True


def remove_rectangle(board, num, block):
    height = len(board)
    left_bottom, right_top = block['coordinate']
    for x in range(left_bottom[1], right_top[1] + 1):
        for y in range(height):
            if board[y][x] == num or board[y][x] == -1:
                board[y][x] = 0

    find_available(board, left_bottom[1], right_top[1] + 1)


def print_board(board):
    height = len(board)
    width = len(board[0])

    for y in range(height):
        row = list(map(lambda x: str(x).zfill(2), board[y]))
        print(' '.join(row))


def solution(board):
    answer = 0
    blocks = find_block(board)
    find_available(board, 0, len(board[0]))
    print_board(board)

    while True:
        flag = True
        for num in blocks:
            if is_rectangle(board, num, blocks[num]):
                flag = False
                answer += 1
                remove_rectangle(board, num, blocks[num])
        print()
        print_board(board)
        if flag:
            break
    return answer


if __name__ == '__main__':
    # print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
    #                 [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
    #                 [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
    #                 [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
    #                 [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
    #                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))

    print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 3, 4, 4, 0, 0, 0],
                    [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
                    [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
                    [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
