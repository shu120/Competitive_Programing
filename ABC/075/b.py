#B - Minesweeper
H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = [[''] * W for _ in range(H)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(H):
	for j in range(W):
		if S[i][j] == '#':
			ans[i][j] = '#'
			continue

		cnt = 0
		for k in range(8):
			ni = i + dx[k]
			nj = j + dy[k]

			if 0 <= ni < H and 0 <= nj < W:
				if S[ni][nj] == '#':
					cnt += 1

		ans[i][j] = str(cnt)

for row in ans:
	print(''.join(row))
