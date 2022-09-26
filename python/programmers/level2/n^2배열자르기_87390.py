def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        y = idx // n
        x = idx % n
        answer.append(max(y + 1, x + 1))
    return answer


if __name__ == '__main__':
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))
