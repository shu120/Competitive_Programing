N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = 0
for i in P:
	if i % K == 0:
		ans += i

print(ans)