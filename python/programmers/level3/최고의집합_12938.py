from functools import reduce
from itertools import product
from operator import mul


def solution(n, s):
    pivot = s // n
    if pivot == 0:
        return [-1]

    mod = s % n
    answer = [pivot] * n

    for i in range(mod):
        answer[n - i - 1] += 1

    return answer



def solution_bak(n, s):
    _product = product([i for i in range(1, s + 1)], repeat=n)
    _filter = list(filter(lambda x: sum(x) == s, _product))
    if len(_filter) == 0:
        return [-1]

    _max = -1
    answer = []
    for _set in _filter:
        _sum = reduce(mul, _set, 1)
        if _max < _sum:
            _max = _sum
            answer = list(_set)
    return answer


if __name__ == '__main__':
    print(solution(2, 9))
    print(solution(2, 1))
    print(solution(2, 8))
    print(solution(3, 9))
    print(solution(3, 8))
