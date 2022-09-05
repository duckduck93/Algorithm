def solution(jobs):
    """
    1. 요청시간 순으로 정렬 jobs = sort(jobs)
    2. 현재 가능한 job 찾기 available = filter(jobs)
    3. 가능한 job 이 없는 경우 timer = jobs[0].req & continue
    4. 가능한 job 중 finish가 가장 짧은 job 찾기 next = sort(jobs, by finish)
    5. 처리한 job 제거
    """
    jobs = sorted(jobs, key=lambda arg: arg[0])
    for job in jobs:
        job.append(0)

    job_count = len(jobs)
    timer = 0
    answer = 0

    while jobs:
        available = list(filter(lambda arg: not arg[3] and arg[0] <= timer, jobs))
        if len(available) == 0:
            timer = jobs[0][0]
            continue

        for job in available:
            job[2] = timer + job[1]  # timer + duration
        next_job = sorted(available, key=lambda arg: arg[2]).pop(0)
        timer += next_job[1]
        answer += next_job[2] - next_job[0]
        jobs.remove(next_job)

    return int(answer / job_count)
