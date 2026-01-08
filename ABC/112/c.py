N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

for x0, y0, h0 in data:
	if h0 > 0:
		base = (x0, y0, h0)
		break

bx, by, bh = base

for cx in range(101):
	for cy in range(101):
		H = bh + abs(bx - cx) + abs(by - cy)

		ok = True
		for x, y, h in data:
			pred = max(H - abs(x - cx) - abs(y - cy), 0)
			if pred != h:
				ok = False
				break

		if ok:
			print(cx, cy, H)
			exit()