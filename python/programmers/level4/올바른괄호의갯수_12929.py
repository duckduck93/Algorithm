def solution(n):
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for count in range(2, n + 1):
        for i in range(count):
            dp[count] += dp[i] * dp[count - i - 1]
    return dp[n]


if __name__ == '__main__':
    for i in range(2, 6):
        print(solution(i))
