from collections import deque

jobs = [int(x) for x in input().split(", ")]
job_idx = int(input())

job_cycles = jobs.pop(job_idx)
jobs.insert(job_idx, "X")
jobs = deque(jobs)
cycles = job_cycles

while jobs:
    current_job = jobs.popleft()
    
    if current_job == "X":
        continue

    if current_job < job_cycles:
        cycles += current_job

    elif current_job == job_cycles and "X" in jobs:
        cycles += current_job

print(cycles)
