# python3
import heapq

def parallel_processing(a, b, data):
    output = []
    hep = [(0, i) for i in range(a)]
    heapq.heapify(hep)
    for i in range(b):
        t, thread = heapq.heappop(hep)
        start = t
        finish = t + data[i]
        output.append((thread, start))
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
