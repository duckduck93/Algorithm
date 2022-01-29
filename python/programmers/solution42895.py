def init_set(arg):
    result = set()
    result.add(arg)
    return result


def solution(N, number):
    answer = -1
    sets = []
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))
        for j in range(0, i - 1):

            for operand1 in sets[j]:
                for operand2 in sets[-j-1]:
                    numbers.add(operand1 + operand2)
                    numbers.add(operand1 - operand2)
                    numbers.add(operand1 * operand2)
                    if operand2 != 0:
                        numbers.add(operand1 // operand2)

        if number in numbers:
            answer = i
            break

        sets.append(numbers)

    return answer


if __name__ == '__main__':
    print(solution(5, 12))
    print(solution(5, 31168))
    print(solution(2, 11))
