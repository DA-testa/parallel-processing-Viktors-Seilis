# Viktors Valdis Seilis
# 221RDB406
# python3
import heapq 

def parallel_processing(a, b, data):
    output = [] # Make a empty list
    hep = [(0, i) for i in range(a)] # Defines the thread count and there starting time
    heapq.heapify(hep) # Heap is converted into a priority queue
    for i in range(b):
        t, thread = heapq.heappop(hep) # Make that thread with with the earliest available time is always at the top of the heap.
        start = t 
        finish = t + data[i] 
        # Thread is appended to the output list, representing the assignment of the current task to a thread and its start time.
        output.append((thread, start)) 
        # Thread is pushed back into the heap using heappush, ensuring that the heap remains updated with the new available time for the thread after processing the current task.
        heapq.heappush(hep, (finish, thread)) 
    return output

def main():
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(a, b, data)
    for thread, start in result:
        print(thread, start)


if __name__ == "__main__":
    main()
