def solution(cookie):
    length = len(cookie)
    answer = 0
    for m in range(length - 1):
        l_sum, l_idx = cookie[m], m
        r_sum, r_idx = cookie[m + 1], m + 1

        while True:
            if l_sum == r_sum:
                answer = max(answer, l_sum)

            if l_idx > 0 and l_sum <= r_sum:
                l_idx -= 1
                l_sum += cookie[l_idx]
            elif r_idx < length - 1 and l_sum >= r_sum:
                r_idx += 1
                r_sum += cookie[r_idx]
            else:
                break

    return answer


def solution_bak(cookie):
    length = len(cookie)
    answer = 0
    for i in range(1, length):
        for m in range(i, length):
            for r in range(m + 1, length):
                if sum(cookie[i:m + 1]) == sum(cookie[m + 1: r + 1]):
                    answer = max(answer, sum(cookie[i:m + 1]))
                    # print(i, m, '|', m + 1, r, '|', cookie[i:m+1], '|', cookie[m + 1: r+1])

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 2, 3]))
    print(solution([1, 2, 4, 5]))
