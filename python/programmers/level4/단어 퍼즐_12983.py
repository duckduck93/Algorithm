import sys


def solution(strs, t):
    dp = [sys.maxsize] * (len(t) + 1)
    for i in range(1, len(t) + 1):
        word = t[:i]
        for s in strs:
            if not word.endswith(s):
                continue
            if len(word) == len(s):
                dp[i] = 1
            else:
                dp[i] = min(dp[i], dp[i - len(s)] + 1)

    return dp[len(t)] if dp[len(t)] != sys.maxsize else -1


if __name__ == '__main__':
    print(solution(["ba", "na", "n", "a"], "banana"))
    print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
    print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
