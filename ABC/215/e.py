# E - Chain Contestant
N = int(input())
S = input()

MOD = 998244353
NONE = 10

dp = [[0] * 11 for _ in range(1 << 10)]
dp[0][NONE] = 1

for c in S:
    x = ord(c) - ord("A")

    ndp = [[0] * 11 for _ in range(1 << 10)]

    for mask in range(1 << 10):
        for last in range(11):
            val = dp[mask][last]

            if val == 0:
                continue

            ndp[mask][last] += val

            if last == NONE:
                ndp[0][x] += val

            elif last == x:
                ndp[mask][x] += val

            elif mask >> x & 1:
                continue

            else:
                ndp[mask | (1 << last)][x] += val

            ndp[mask][last] %= MOD

    dp = ndp

ans = 0

for mask in range(1 << 10):
    for last in range(11):
        ans += dp[mask][last]

print((ans - 1) % MOD)
