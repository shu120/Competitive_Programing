#D
from collections import deque

H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]

ALPHABET = 26
A_ORD = ord('a')

warp_positions = [[] for _ in range(ALPHABET)]
for i in range(H):
	for j in range(W):
		cell = grid[i][j]
		if 'a' <= cell <= 'z':
			warp_positions[ord(cell) - A_ORD].append((i, j))

INF = 10 ** 18
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0
queue  = deque([(0, 0)])
warp_used = [False] * ALPHABET

while queue:
	r, c = queue.popleft()
	curr_dist = dist[r][c]

	if r == H - 1 and c == W - 1:
		break

	for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		nr, nc = r + dr, c + dc
		if 0 <= nr < H and 0<= nc < W and grid[nr][nc] != '#':
			if dist[nr][nc] > curr_dist + 1:
				dist[nr][nc] = curr_dist + 1
				queue.append((nr, nc))
	
	cell = grid[r][c]
	if 'a' <= cell <= 'z':
		idx = ord(cell) - A_ORD
		if not warp_used[idx]:
			warp_used[idx] = True
			for nr, nc in warp_positions[idx]:
				if dist[nr][nc] > curr_dist + 1:
					dist[nr][nc] = curr_dist + 1
					queue.append((nr, nc))

result = dist[H - 1][W - 1]
print(-1 if result == INF else result)