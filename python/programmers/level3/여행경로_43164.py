from collections import defaultdict


def ticket_dictionary(tickets):
    ticket_dict = defaultdict(list)
    for departure, destination in tickets:
        ticket_dict[departure].append({'destination': destination, 'is_used': False})
    for departure in ticket_dict:
        ticket_dict[departure].sort(key=lambda arg: arg['destination'])
    return ticket_dict


def dfs(ticket_dict, total_count, departure="ICN", count=0, ):
    if total_count == count:
        return [departure]

    next_tickets = ticket_dict[departure]
    for ticket in next_tickets:
        destination, is_used = ticket['destination'], ticket['is_used']
        if is_used:
            continue
        ticket['is_used'] = True
        result = dfs(ticket_dict, total_count, destination, count + 1)

        if result is None:
            ticket['is_used'] = False
            continue

        result.insert(0, departure)
        return result
    return None


def solution(tickets):
    ticket_dict = ticket_dictionary(tickets)
    return dfs(ticket_dict, len(tickets))


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
