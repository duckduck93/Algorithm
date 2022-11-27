from itertools import product


def make_dictionary():
    chars = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    for i in range(1, 6):
        items = list(map(lambda arg: ''.join(arg), product(chars, repeat=i)))
        dictionary.extend(items)

    return sorted(dictionary)


def solution(word):
    dictionary = make_dictionary()
    return dictionary.index(word) + 1


if __name__ == '__main__':
    print(solution("AAAAE", ))
    print(solution("AAAE", ))
    print(solution("I", ))
    print(solution("EIO", ))
