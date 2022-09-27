def solution(dirs):
    result = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d[dir][0], y + d[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            result.add((x, y, nx, ny))
            result.add((nx, ny, x, y))
            x, y = nx, ny
    return len(result) // 2


if __name__ == '__main__':
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
