S = input()
MOD = 998244353

idx = {"a": 0, "b": 1, "c": 2}
dp = [0, 0, 0]

for ch in S:
    x = idx[ch]

    add = 1
    for y in range(3):
        if y != x:
            add += dp[y]

    dp[x] += add
    dp[x] %= MOD

print(sum(dp) % MOD)
