from collections import deque

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

row_b = [False] * H
col_b = [False] * W

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            row_b[i] = True
            col_b[j] = True

dist = [[-1] * W for _ in range(H)]
que = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not row_b[i] and not col_b[j]:
            dist[i][j] = 0
            que.append((i, j))

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

while que:
    i, j = que.popleft()

    if dist[i][j] == K:
        continue

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if not (0 <= ni < H and 0 <= nj < W):
            continue

        if S[ni][nj] == "#":
            continue

        if dist[ni][nj] != -1:
            continue

        dist[ni][nj] = dist[i][j] + 1
        que.append((ni, nj))

ans = 0

for i in range(H):
    for j in range(W):
        if dist[i][j] != -1:
            ans += 1

print(ans)
