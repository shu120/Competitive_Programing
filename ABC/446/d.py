import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = {}
ans = 0

for x in A:
	dp[x] = dp.get(x - 1, 0) + 1
	ans = max(ans, dp[x])

print(ans)