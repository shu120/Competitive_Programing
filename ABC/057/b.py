n, m = map(int, input().split())
stud = [tuple(map(int, input().split())) for _ in range(n)]
chec = [tuple(map(int, input().split())) for _ in range(m)]

for sx, sy in stud:
	mindist = 10**18
	idx = -1
	for j, (cx, cy) in enumerate(chec, start = 1):
		dist = abs(cx - sx) + abs(cy - sy)
		if dist < mindist:
			mindist = dist
			idx = j
	print(idx)