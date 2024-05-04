import controller as cnt
import time
def fcfs_scheduling(burst_time):
    
    n = len(burst_time)
    waiting_time = [0] * n
    process_order = list(range(n))  

    t = 0

    for i in range(n):
        t += burst_time[i]
        waiting_time[i] = t - burst_time[i] 
    for i in range(len(process_order)):
        cnt.led2(process_order[i])
        time.sleep(1.5)
    return waiting_time, process_order
