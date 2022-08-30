def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    person = {}
    for i, e in enumerate(enroll):
        person[e] = i
    for parent, a in zip(seller, amount):
        earn = a * 100
        while parent != "-" and earn > 0:
            idx = person[parent]
            money[idx] += earn - earn//10
            earn //= 10
            parent = referral[idx]
    return money


if __name__ == '__main__':
    print(solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10]
    ))
    print(solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["sam", "emily", "jaimie", "edward"],
        [2, 3, 5, 4]
    ))
