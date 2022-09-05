def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        answer += num if sign else -num
    return answer


if __name__ == '__main__':
    print(solution([4, 7, 12], [True, False, True]))
