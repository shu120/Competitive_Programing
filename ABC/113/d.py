# D - Number of Amidakuji
H, W, K = map(int, input().split())
MOD = 1000000007

dp = [0] * W
dp[0] = 1

for _ in range(H):
    ndp = [0] * W

    for mask in range(1 << (W - 1)):
        if mask & (mask << 1):
            continue

        for j in range(W):
            if j < W - 1 and mask >> j & 1:
                ndp[j + 1] += dp[j]
            elif j > 0 and mask >> (j - 1) & 1:
                ndp[j - 1] += dp[j]
            else:
                ndp[j] += dp[j]

    dp = [x % MOD for x in ndp]

print(dp[K - 1])
