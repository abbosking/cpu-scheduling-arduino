import controller as cnt
import time
def round_robin(burst_time, quantum):
    n = len(burst_time)
    waiting_time = [0] * n
    remaining_burst_time = list(burst_time)
    process_order = []\

    t = 0  # Current time
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                process_order.append(i) 
                if remaining_burst_time[i] > quantum:
                    t += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    t += remaining_burst_time[i]
                    waiting_time[i] = t - burst_time[i]
                    remaining_burst_time[i] = 0
        if done:
            break

    for i in range(len(process_order)):
        cnt.led2(process_order[i])
        time.sleep(1.5)
    return waiting_time, process_order
