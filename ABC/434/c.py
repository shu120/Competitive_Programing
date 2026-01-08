#C
T = int(input())

for _ in range(T):
	N, H = map(int, input().split())
	goal = [tuple(map(int, input().split())) for _ in range(N)]
	goal.sort()

	low = high = H
	last = 0
	ok = True

	for t, l ,u in goal:
		dt = t - last
		low -= dt
		high += dt
		if low < 0:
			low = 0
		
		low = max(low, l)
		high = min(high, u)

		if low > high:
			ok = False
			break

		last = t
	
	print("Yes" if ok else "No")