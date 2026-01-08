#C
N, M = map(int, input().split())
placed = set()
count = 0

for _ in range(M):
	r, c = map(int, input().split())
	r -= 1
	c -= 1
	cells = [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]
	can_place = True
	for cell in cells:
		if cell in placed:
			can_place = False
			break
	if can_place:
		for cell in cells:
			placed.add(cell)
		count += 1

print(count)