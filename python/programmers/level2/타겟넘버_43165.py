def solution(numbers, target):
    results = [0]
    for num in numbers:
        temp = []
        for parent in results:
            temp.append(parent + num)
            temp.append(parent - num)
        results = temp

    answer = 0
    for arg in results:
        answer += 1 if arg == target else 0
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
