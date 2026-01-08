#B
N = int(input().strip())

a = [[0] * N for _ in range(N)]

r, c = 0, (N - 1) // 2
a[r][c] = 1

for k in range(2, N * N + 1):
	nr = (r - 1) % N
	nc = (c + 1) % N
	if a[nr][nc] == 0:
		r, c = nr, nc
	else:
		r = (r + 1) % N
	a[r][c] = k

for i in range(N):
	print(*a[i])
