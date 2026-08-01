# E - Stronger Takahashi
from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = float("inf")
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0

q = deque([(0, 0)])

move = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

while q:
    r, c = q.popleft()
    curr = dist[r][c]

    for dr, dc in move:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < H and 0 <= nc < W):
            continue

        if S[nr][nc] == "#":
            continue

        if dist[nr][nc] <= curr:
            continue

        dist[nr][nc] = curr
        q.appendleft((nr, nc))

    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) == 2 and abs(dc) == 2:
                continue

            nr = r + dr
            nc = c + dc

            if not (0 <= nr < H and 0 <= nc < W):
                continue

            if dist[nr][nc] <= curr + 1:
                continue

            dist[nr][nc] = curr + 1
            q.append((nr, nc))

print(dist[H - 1][W - 1])
