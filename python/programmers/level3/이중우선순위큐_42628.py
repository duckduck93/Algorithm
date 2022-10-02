from queue import PriorityQueue


def solution(operations):
    asc_queue = PriorityQueue()
    desc_queue = PriorityQueue()
    items = {}
    for op in operations:
        [action, value] = op.split(' ')
        if action == 'I':
            asc_queue.put(int(value))
            desc_queue.put(int(value) * -1)
            items[value] = True
        elif action == 'D' and value == '-1':
            pop = None
            while not asc_queue.empty():
                pop = asc_queue.get()
                if items[str(pop)]:
                    break
            items[str(pop)] = False
        elif action == 'D' and value == '1':
            pop = None
            while not desc_queue.empty():
                pop = desc_queue.get() * -1
                if items[str(pop)]:
                    break
            items[str(pop)] = False

    alive_items = list(filter(lambda item: item, list(items.values())))
    if len(alive_items) == 0:
        return [0, 0]

    min_value = None
    while not asc_queue.empty():
        pop = asc_queue.get()
        if items[str(pop)]:
            min_value = pop
            break

    max_value = None
    while not desc_queue.empty():
        pop = desc_queue.get() * -1
        if items[str(pop)]:
            max_value = pop
            break

    answer = [max_value, min_value]
    return answer


if __name__ == '__main__':
    # print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
