N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
for i in range(N):
	if A[i] == K:
		ans = i + 1
		break

print(ans)