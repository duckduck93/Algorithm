import math


def solution(fees, records):
    charge = {}
    for record in records:
        [time, car, action] = record.split(' ')
        time_arr = time.split(':')
        time = int(time_arr[0]) * 60 + int(time_arr[1])

        if car not in charge.keys():
            charge[car] = []
        charge[car].append([time, action])

    for car in charge:
        last_action = charge[car][-1][-1]
        if last_action == 'IN':
            charge[car].append([1439, 'OUT'])

        result = 0
        for idx, time in enumerate(charge[car]):
            if idx % 2 == 0:
                result -= time[0]
            else:
                result += time[0]

        [default_time, default_charge, per_time, per_charge] = fees
        charge[car] = default_charge
        charge[car] += math.ceil(max(result - default_time, 0) / per_time) * per_charge

    answer = []
    for car in sorted(charge.keys()):
        answer.append(charge[car])
    return answer


if __name__ == '__main__':
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

    print(solution([120, 0, 60, 591],
                   ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
