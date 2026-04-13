#D - Grid Repainting
from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

def gridbfs(grid, H, W):
    dist = [[-1] * W for _ in range(H)]
    dist[0][0] = 1

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

white = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            white += 1

ans = -1
dist = gridbfs(grid, H, W)

if dist[H - 1][W - 1] == -1:
    print(ans)
else:
    ans = white - dist[H - 1][W - 1]
    print(ans)
