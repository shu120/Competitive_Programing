#008 - AtCounter（★4）
N = int(input())
S = input()

MOD = 10 ** 9 + 7
T = "atcoder"
dp = [0] * (len(T) + 1)
dp[0] = 1

for i in S:
	for j in range(len(T) - 1, -1, -1):
		if i == T[j]:
			dp[j + 1] = (dp[j + 1] + dp[j]) % MOD

print(dp[len(T)] % MOD)