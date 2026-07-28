#D - XXOR
N, K = map(int, input().split())
A = list(map(int, input().split()))

INF = float("-inf")
dp = [0, INF]

for b in range(40, -1, -1):
    cnt = sum(a >> b & 1 for a in A)

    val0 = cnt * (1 << b)
    val1 = (N - cnt) * (1 << b)

    ndp = [INF, INF]
    kb = K >> b & 1

    for smaller in range(2):
        if dp[smaller] == INF:
            continue

        for xb in range(2):
            if not smaller and xb > kb:
                continue

            nxt = smaller or xb < kb
            val = val1 if xb else val0

            ndp[nxt] = max(ndp[nxt], dp[smaller] + val)

    dp = ndp

print(max(dp))
