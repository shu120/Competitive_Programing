N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
	if sum(map(int, str(i))) == K:
		ans += 1

print(ans)