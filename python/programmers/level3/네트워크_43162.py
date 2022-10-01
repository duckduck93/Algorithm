def find_connected_computers(n, computers, idx):
    if computers[idx][idx] == 0:
        return None

    result = [idx]
    for com in computers:
        com[idx] = 0

    for connection in range(n):
        if idx == connection:
            continue
        if computers[idx][connection] == 0:
            continue
        result.extend(find_connected_computers(n, computers, connection))
    return result


def solution(n, computers):
    all_connections = []
    for i in range(n):
        network = find_connected_computers(n, computers, i)
        if network is not None:
            all_connections.append(network)
    # print(all_connections)
    return len(all_connections)


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
