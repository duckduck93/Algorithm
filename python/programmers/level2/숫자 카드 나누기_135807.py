import math


def find_common_divisor(array):
    result = []
    min_arg = array[0]
    for i in range(2, min_arg + 1):
        flag = True
        for arg in array:
            if arg % i != 0:
                flag = False
                break
        if flag:
            result.append(i)
    return result


def solution_bak(arrayA, arrayB):
    arrayA = sorted(list(set(arrayA)))
    arrayB = sorted(list(set(arrayB)))

    cd_a = sorted(find_common_divisor(arrayA), reverse=True)
    cd_b = sorted(find_common_divisor(arrayB), reverse=True)

    a = find_non_divisor(arrayB, cd_a)
    b = find_non_divisor(arrayA, cd_b)

    return max(a, b)


def find_gcd(array):
    gcd = array[0]
    for arg in array:
        gcd = math.gcd(gcd, arg)
    return gcd


def find_non_divisor(array, cd_array):
    result = 0
    for cd in cd_array:
        flag = True
        for arg in array:
            if arg % cd == 0:
                flag = False
                break
        if flag:
            result = max(result, cd)
            break
    return result


def solution(arrayA, arrayB):
    cd_a = find_gcd(arrayA)
    cd_b = find_gcd(arrayB)

    a = find_non_divisor(arrayB, [cd_a])
    b = find_non_divisor(arrayA, [cd_b])

    return max(a, b)


if __name__ == '__main__':
    print(solution([10, 17], [5, 20]))
    print(solution([10, 20], [5, 17]))
    print(solution([14, 35, 119], [18, 30, 102]))
