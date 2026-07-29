# E - Safety Journey
MOD = 998244353

N, M, K = map(int, input().split())

edge = []

for _ in range(M):
    u, v = map(int, input().split())
    edge.append((u - 1, v - 1))

dp = [0] * N
dp[0] = 1

for _ in range(K):
    total = sum(dp) % MOD

    ndp = [total] * N

    for v in range(N):
        ndp[v] -= dp[v]

    for u, v in edge:
        ndp[u] -= dp[v]
        ndp[v] -= dp[u]

    for v in range(N):
        ndp[v] %= MOD

    dp = ndp

print(dp[0])
