from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

event = defaultdict(int)

cost = 0
slope = 0
sign = 1
c = 0

for i in range(N):
    if sign == 1:
        p = (A[i] - c) % M

        cost += (-p) % M
        slope += 1

        if p > 0:
            event[p - 1] -= M

    else:
        q = (c - A[i]) % M

        cost += q
        slope -= 1

        if q < M - 1:
            event[q] += M

    if i < N - 1:
        sign *= -1
        c = (B[i] - c) % M

ans = cost
x = 0

for pos in sorted(event):
    cost += slope * (pos - x)
    ans = min(ans, cost)

    cost += slope + event[pos]
    x = pos + 1

    ans = min(ans, cost)

cost += slope * (M - 1 - x)
ans = min(ans, cost)

print(ans)
