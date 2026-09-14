# D - Between Two Arrays
MOD = 998244353
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

MAX = 3000

dp = [0] * (MAX + 1)

for x in range(a[0], b[0] + 1):
    dp[x] = 1

for i in range(1, N):
    ndp = [0] * (MAX + 1)
    s = 0

    for x in range(MAX + 1):
        s += dp[x]
        s %= MOD

        if a[i] <= x <= b[i]:
            ndp[x] = s

    dp = ndp

print(sum(dp) % MOD)
