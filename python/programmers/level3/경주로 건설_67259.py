import pprint
import sys
from collections import deque


def print_money(money):
    for row in money:
        for cell in row:
            print(str(cell).zfill(6) if cell != sys.maxsize else '------', end=' ')
        print()
    print()


def bfs(board, init):
    width = len(board)
    next_move = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    money = [[sys.maxsize for _ in range(width)] for _ in range(width)]
    money[0][0] = 0

    q = deque()
    q.append(init)

    while q:
        y, x, cost, direction = q.popleft()
        for move in next_move:
            dy, dx, next = move
            ny, nx, = y + dy, x + dx
            next_cost = cost + 100 if direction == next else cost + 600
            if 0 <= ny < width and 0 <= nx < width and board[ny][nx] == 0 and money[ny][nx] >= next_cost:
                money[ny][nx] = next_cost
                q.append((ny, nx, next_cost, next))

    print_money(money)
    return money[-1][-1]


def solution(board):
    return min(bfs(board, (0, 0, 0, 'D')), bfs(board, (0, 0, 0, 'R')))


# print(900, solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print()
print(3800, solution(
    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
print()
print(2100, solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
print()
print(3200, solution(
    [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]))
print()
