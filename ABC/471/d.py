import heapq

Q, V = map(int, input().split())

hq = []

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        _, t, w = q
        heapq.heappush(hq, -(w - t))

    else:
        _, t = q

        if not hq:
            print(-1)
            continue

        x = -heapq.heappop(hq)
        print(min(V, t + x))
