# Name: M. Saad Bin Shafiq
# Reg No: 200901079
# Batch: BSCS-01-B

# ROUND ROBIN SCHEDULING ALGORITHM

# Calculating Waiting Time
def findWaitingTime(process_id, n, burstTime, waitingTime, quantum):
    rem_burstTime = [0] * n

    for i in range(n):
        rem_burstTime[i] = burstTime[i]

        # Current time
    time = 0

    # Now Traversing according to RR
    while (1):
        done = True

        # Traversing through all processes one by one
        for i in range(n):

            # If burst time > 0 then only need to process further
            if (rem_burstTime[i] > 0):

                done = False

                if (rem_burstTime[i] > quantum):

                    # Increase the value of time i.e. shows how much time a process has been processed
                    time += quantum

                    # Decrease the burst time of current process by quantum
                    rem_burstTime[i] -= quantum

                    # If burst time <= quantum. Last cycle for this process
                else:

                    # Increase the value of time i.e. shows how much time a process has been processed
                    time = time + rem_burstTime[i]

                    # Waiting time = time - burstTime
                    waitingTime[i] = time - burstTime[i]

                    # As the process gets fully executed make its remaining burst time = 0
                    rem_burstTime[i] = 0

        # If all processes are done
        if (done == True):
            break


# Function to calculate turn around time
def findTurnAroundTime(process_id, n, burstTime, waitingTime, turnAroundTime):
    # Calculating turnaround time
    for i in range(n):
        turnAroundTime[i] = burstTime[i] + waitingTime[i]

# Function to calculate average waiting time and turn around time

def findavgTime(process_id, n, burstTime, quantum):
    waitingTime = [0] * n
    turnAroundTime = [0] * n

    # Function to find waiting time of all processes
    findWaitingTime(process_id, n, burstTime, waitingTime, quantum)

    # Function to find turn around time for all processes
    findTurnAroundTime(process_id, n, burstTime, waitingTime, turnAroundTime)

    print("Processes", "  Burst Time", "  Waiting Time", "  Turn Around Time")
    total_waitingTime = 0
    total_turnAroundTime = 0
    for i in range(n):
        total_waitingTime = total_waitingTime + waitingTime[i]
        total_turnAroundTime = total_turnAroundTime + turnAroundTime[i]
        print("   ", i + 1, "         ", burstTime[i], "            ", waitingTime[i], "            ",
              turnAroundTime[i])

        # Display average times of processes
    print("\nAverage Waiting Time = %.5f " % (total_waitingTime))
    print("Average Turn Around Time = %.5f " % (total_turnAroundTime))


# Driver code
if __name__ == '__main__':
    total_processes = int(input("Enter no of processes: "))
    process_id = []
    burst_time = []
    for i in range(0, total_processes):
        x = int(input("Enter process id:"))
        process_id.append(x)
        y = int(input("Enter Burst time:"))
        burst_time.append(y)
        print()

# Here we adjust the time quantum to '3'
    quantum = 3
    findavgTime(process_id, x, burst_time, quantum)