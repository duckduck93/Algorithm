def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 1:
            answer += 1
        n = int(n / 2)
    return answer


def solution_bak(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(n + 1):
        if i % 2 == 0:
            arr[i] = arr[int(i / 2)]
        else:
            arr[i] = arr[i - 1] + 1
    return arr[n]


if __name__ == '__main__':
    print(solution(5000))
