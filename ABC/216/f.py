# F - Max Sum Counting
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353
MAX = 5000

AB = sorted(zip(A, B))

dp = [0] * (MAX + 1)
dp[0] = 1

ans = 1

for a,b in AB:
    if a >= b:
        ans += sum(dp[:a - b + 1])
        ans %= MOD

    for s in range(MAX - b, -1, -1):
        dp[s + b] += dp[s]
        dp[s + b] %= MOD

print(ans)
