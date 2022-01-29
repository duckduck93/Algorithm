def solution(triangle):
    dp = []

    for level, _ in enumerate(triangle):
        if level == 0:
            dp.append(triangle[level])
            continue

        pre_row = dp[level - 1]
        cur_row = triangle[level]
        dp_row = []
        for col, _ in enumerate(cur_row):
            if col == 0:
                dp_row.append(pre_row[col] + cur_row[col])
                continue
            if col == len(cur_row) - 1:
                dp_row.append(pre_row[col - 1] + cur_row[col])
                continue

            dp_row.append(max(pre_row[col - 1], pre_row[col]) + cur_row[col])
        dp.append(dp_row)

    return max(dp[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
