import controller as cnt
import time
def shortest_job_first(burst_time):

    n = len(burst_time)
    waiting_time = [0] * n
    process_order = []

    # Create a copy of burst time to avoid modifying the original list
    sorted_burst_time = burst_time.copy()

    # Sort processes by burst time (ascending order)
    sorted_indexes = sorted(range(len(sorted_burst_time)), key=sorted_burst_time.__getitem__)

    t = 0  # Current time

    for i in sorted_indexes:
        t += sorted_burst_time[i]
        waiting_time[i] = t - sorted_burst_time[i]
        process_order.append(i)

    for i in range(len(process_order)):
        cnt.led2(process_order[i])
        time.sleep(1.5)
    return waiting_time, process_order
