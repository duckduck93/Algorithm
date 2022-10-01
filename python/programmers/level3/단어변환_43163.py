import pprint
import sys


def word_diff(arg, tar):
    diff = 0
    for idx in range(len(arg)):
        if arg[idx] == tar[idx]:
            continue
        diff += 1
    return diff


def find_next_words(begin, target, words, visit, count):
    if begin == target:
        return {'child':[begin], 'cnt': count}

    result = {'child': [], 'cnt': sys.maxsize}
    for idx in range(len(words)):
        if visit[idx]:
            continue
        if word_diff(begin, words[idx]) != 1:
            continue
        visit[idx] = True
        next_words = find_next_words(words[idx], target, words, visit, count + 1)
        if len(next_words) != 0:
            result['child'].append(next_words)
            result['cnt'] = min(result['cnt'], next_words['cnt'])
        visit[idx] = False
    return result


def solution(begin, target, words):
    visit = [False] * len(words)
    answer = find_next_words(begin, target, words, visit, 0)
    return answer['cnt'] if answer['cnt'] != sys.maxsize else 0


if __name__ == '__main__':
    pprint.pprint(solution('hit', 'cog', ['hot', 'dot', 'cog']))
    pprint.pprint(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), indent=2)
    pprint.pprint(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    pprint.pprint(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
