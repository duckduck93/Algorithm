def solution(m, n, puddles):
    puddle_map = [[1 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        puddle_map[puddle[1] - 1][puddle[0] - 1] = 0
    for row in range(n):
        for col in range(m):
            if puddle_map[row][col] == 0:
                continue
            if row == 0 and col == 0:
                dp[row][col] = 1
                continue
            if row == 0:
                dp[row][col] = dp[row][col - 1]
                continue
            if col == 0:
                dp[row][col] = dp[row - 1][col]
                continue
            dp[row][col] = (dp[row - 1][col] + dp[row][col - 1]) % 1000000007
    return dp[-1][-1]


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]), 4)
    print(solution(2, 2, []), 2)
    print(solution(3, 3, []), 6)
    print(solution(3, 3, [[2, 2]]), 2)
    print(solution(3, 3, [[2, 3]]), 3)
    print(solution(3, 3, [[1, 3]]), 5)
    print(solution(3, 3, [[1, 3], [3, 1]]), 4)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
    print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
    print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
    print(solution(4, 4, [[3, 2], [2, 4]]), 7)
    print(solution(100, 100, []), 690285631)
