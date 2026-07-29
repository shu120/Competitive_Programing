# D - Querying Multiset
import heapq

Q = int(input())

h = []
add = 0
ans = []

for _ in range(Q):
    q = list(map(int, input().split()))
    p = q[0]

    if p == 1:
        x = q[1]
        heapq.heappush(h, x - add)

    elif p == 2:
        x = q[1]
        add += x

    else:
        ans.append(heapq.heappop(h) + add)

print("\n".join(map(str, ans)))
