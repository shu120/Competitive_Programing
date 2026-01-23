N = int(input())
a = list(map(int, input().split()))

color = set()
free = 0

for i in a:
	if i < 3200:
		color.add(i // 400)
	else:
		free += 1

min_colors = max(1, len(color))
max_colors = len(color) + free

print(min_colors, max_colors)