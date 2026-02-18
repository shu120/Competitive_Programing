import sys
input = sys.stdin.readline
from collections import defaultdict

H, W, N = map(int, input().split())

height_map = defaultdict(list)
width_map = defaultdict(list)

for i in range(N):
	h, w = map(int, input().split())
	height_map[h].append((w, i))
	width_map[w].append((h, i))

used = [False] * N
ans = [None] * N

curH, curW = H, W
xr, yb = W, H

for _ in range(N):
	placed = False

	while height_map[curH]:
		w, idx = height_map[curH].pop()
		if used[idx]:
			continue

		row = 1
		col = xr - w + 1 # 1-index

		ans[idx] = (row, col)

		xr -= w
		curW -= w
		used[idx] = True
		placed = True
		break

	if placed:
		continue

	while width_map[curW]:
		h, idx = width_map[curW].pop()
		if used[idx]:
			continue

		row = yb - h + 1 # 1-index
		col = 1

		ans[idx] = (row, col)

		yb -= h
		curH -= h
		used[idx] = True
		break

for x, y in ans:
	print(x, y)