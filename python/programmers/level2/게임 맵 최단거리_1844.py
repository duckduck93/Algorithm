import sys
from collections import deque


def solution_bfs(maps, visits):
    height, width = len(maps), len(maps[0])
    queue = deque(maxlen=height * width)
    queue.append((height - 1, width - 1, 1))  # y, x, count
    visits[height - 1][width - 1] = True
    while queue:
        y, x, count = queue.popleft()
        # visits[y][x] = True
        if y == 0 and x == 0:
            return count
        for next_position in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
            next_y, next_x = next_position
            if next_y < 0 or next_y >= height:
                continue
            if next_x < 0 or next_x >= width:
                continue
            if maps[next_y][next_x] == 0:
                continue
            if visits[next_y][next_x]:
                continue
            queue.append((next_y, next_x, count + 1))
            visits[next_y][next_x] = True  # ? 이해가 잘 안되네 12에 끼워넣으면 시간 초과, 여기 작성하면 통과
    return -1


def solution_dfs(maps, visits, y, x, counter):
    visits[y][x] = True
    if y == len(maps) - 1 and x == len(maps[0]) - 1:
        return counter

    # 동, 서, 남, 북
    next_arr = [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x), ]
    result = sys.maxsize
    for next_position in next_arr:
        next_y, next_x = next_position
        if next_y < 0 or next_y >= len(maps):
            continue
        if next_x < 0 or next_x >= len(maps[0]):
            continue
        if maps[next_y][next_x] == 0:
            continue
        if visits[next_y][next_x]:
            continue
        next_count = solution_dfs(maps, visits, next_y, next_x, counter + 1)
        result = next_count if next_count != sys.maxsize and next_count < result else result
    visits[y][x] = False
    return result


def solution(maps):
    y, x = len(maps), len(maps[0])
    visited = [[False for _ in range(x)] for _ in range(y)]
    answer = solution_bfs(maps, visited)
    return answer


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
