N = int(input())
a = [0] + [int(input()) for _ in range(N)]

visited = [False] * (N + 1)

curr = 1
ans = 0
while True:
	if curr == 2:
		print(ans)
		break
	if visited[curr]:
		print(-1)
		break

	visited[curr] = True
	curr = a[curr]
	ans += 1