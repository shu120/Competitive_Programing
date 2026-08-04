# F - Substrings
S = input()
MOD = 10**9 + 7

N = len(S)

dp = [0] * (N + 1)
dp[0] = 1

last = {}

for i in range(N):
    c = S[i]

    dp[i + 1] = dp[i]

    if i >= 1:
        dp[i + 1] += dp[i - 1]
    else:
        dp[i + 1] += 1

    if c in last:
        p = last[c]
        if p >= 1:
            dp[i + 1] -= dp[p - 1]
        else:
            dp[i + 1] -= dp[0]

    dp[i + 1] %= MOD

    last[c] = i

print((dp[N] - 1) % MOD)
