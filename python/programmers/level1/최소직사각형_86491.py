def solution(sizes):
    for i, size in enumerate(sizes):
        sizes[i] = sorted(size)
    max_x = -1
    max_y = -1
    for size in sizes:
        max_x = size[0] if max_x < size[0] else max_x
        max_y = size[1] if max_y < size[1] else max_y
    return max_x * max_y


if __name__ == '__main__':
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))