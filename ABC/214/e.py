# E - Packing Under Range Regulations
import heapq

T = int(input())

ans = []

for _ in range(T):
    N = int(input())

    lr = []

    for _ in range(N):
        _l, r = map(int, input().split())
        lr.append((_l, r))

    lr.sort()

    h = []
    idx = 0
    x = 0
    ok = True

    while idx < N or h:
        if not h:
            x = lr[idx][0]

        while idx < N and lr[idx][0] <= x:
            heapq.heappush(h, lr[idx][1])
            idx += 1

        r = heapq.heappop(h)

        if r < x:
            ok = False
            break

        x += 1

    ans.append("yes" if ok else "no")

print("\n".join(ans))
