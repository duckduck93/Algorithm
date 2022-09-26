def convert(n, k):
    if k == 10:
        return str(n)
    result = ''
    while n != 0:
        result += str(n % k)
        n = int(n / k)
    return result[::-1]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    convert_string = convert(n, k)
    arr = list(map(int, filter(lambda x: x != '', convert_string.split('0'))))

    answer = 0
    for arg in arr:
        if is_prime(arg):
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(437674, 3))
    print(solution(110011, 10))
