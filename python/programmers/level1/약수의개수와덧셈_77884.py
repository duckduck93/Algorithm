import math


def find_divisor(num):
    if num == 1:
        return {num}
    result = set()
    for i in range(1, int(num)):
        if num % i == 0:
            result.add(i)
            result.add(int(num / i))
    return result


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisor = find_divisor(i)
        answer += i if len(divisor) % 2 == 0 else -i
    return answer


if __name__ == '__main__':
    print(solution(1, 1))
    print(solution(13, 17))
    print(solution(24, 27))
