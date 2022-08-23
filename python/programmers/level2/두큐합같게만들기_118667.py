from collections import deque


def solution(queue1, queue2):
    org1 = list(queue1)
    org2 = list(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    expect_double = (sum(queue1) + sum(queue2)) / 2
    expect = int((sum(queue1) + sum(queue2)) / 2)
    cal = sum(queue1)

    if expect_double != expect:
        return -1

    counter = 0
    for _ in range((len(queue1) - 1) * 3 + 1):
        if cal > expect:
            pop = queue1.popleft()
            queue2.append(pop)

            cal -= pop
            counter += 1
        elif cal < expect:
            pop = queue2.popleft()
            queue1.append(pop)

            cal += pop
            counter += 1
        else:
            return counter

        if org1 == queue1 and org2 == queue2:
            return -1
    return -1


if __name__ == '__main__':
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    print(solution([1, 1], [1, 4]))
    print(solution([10, 2], [5, 5]))
