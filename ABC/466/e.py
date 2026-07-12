N, K = map(int, input().split())

base = 0
D = []

for _ in range(N):
    a, b = map(int, input().split())
    base += a
    D.append(b - a)

INF = 10 ** 18
dp0 = [-INF] * (K + 1)
dp1 = [-INF] * (K + 1)

dp0[0] = 0

for d in D:
    ndp0 = [-INF] * (K + 1)
    ndp1 = [-INF] * (K + 1)

    for k in range(K + 1):
        if dp0[k] != -INF:
            ndp0[k] = max(ndp0[k], dp0[k])

        if dp1[k] != -INF:
            ndp0[k] = max(ndp0[k], dp1[k])

        if dp1[k] != -INF:
            ndp1[k] = max(ndp1[k], dp1[k] + d)

        if k < K and dp0[k] != -INF:
            ndp1[k + 1] = max(ndp1[k + 1], dp0[k] + d)

    dp0, dp1 = ndp0, ndp1

ans = max(max(dp0), max(dp1))
print(base + ans)
