def find_sequence(arg):
    sequence = [arg]
    while arg > 1:
        if arg % 2 == 0:
            arg = arg // 2
        else:
            arg = (arg * 3) + 1
        sequence.append(arg)
    print(sequence)
    return sequence


def find_area(sequence):
    area = []
    for idx in range(len(sequence) - 1):
        cur, nex = sequence[idx], sequence[idx + 1]
        area.append((cur + nex) / 2)
    print(area)
    return area


def solution(k, ranges):
    sequence = find_sequence(k)
    area = find_area(sequence)

    answer = []
    for query in ranges:
        sta, end = query
        end = len(area) + end
        result = sum(area[sta:end]) if sta <= end else -1
        answer.append(result)
        print((sta, end), result)
    return answer


if __name__ == '__main__':
    print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
