from itertools import permutations


def solution(k, dungeons):
    length = len(dungeons)
    comb = list(permutations(range(length), length))

    answer = []
    for path in comb:
        health = k
        count = 0
        for node in path:
            required, remove = dungeons[node]
            if health >= required:
                health -= remove
                count += 1
        answer.append(count)

    return max(answer)


if __name__ == '__main__':
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
