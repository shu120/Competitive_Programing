#C - ソーシャルゲーム
N, M = map(int, input().split())

lot = []

for _ in range(M):
    C, cost = map(int, input().split())

    tmp = []
    for _ in range(C):
        idol, p = map(int, input().split())
        tmp.append((idol - 1, p))

    lot.append((cost, tmp))

INF = float("inf")
dp = [INF] * (1 << N)
dp[-1] = 0.0

for s in range((1 << N) - 2, -1, -1):
    for cost, tmp in lot:
        prob = 0
        curr = cost * 100

        for idol, p in tmp:
            if s >> idol & 1:
                continue
            prob += p
            curr += p * dp[s | (1 << idol)]

        if prob:
            dp[s] = min(dp[s], curr / prob)

print(dp[0])
