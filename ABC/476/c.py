import heapq

N = int(input())
A = list(map(int, input().split()))

hq = []

for i in range(N):
    heapq.heappush(hq, A[i])

    if len(hq) > 3:
        heapq.heappop(hq)
    if i >= 2:
        print(hq[0])
