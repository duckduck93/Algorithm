def number_to_binary_string(num):
    result = ''
    while num != 0:
        result += str(num % 2)
        num = int(num / 2)
    return result[::-1]


def solution(s):
    count = 0
    zero_count = 0
    while s != '1':
        pre_length = len(s)
        cur_length = len(s.replace('0', ''))
        s = number_to_binary_string(cur_length)

        zero_count += pre_length - cur_length
        count += 1

    return [count, zero_count]


if __name__ == '__main__':
    print(solution('110010101001'))
    print(solution('01110'))
    print(solution('1111111'))
