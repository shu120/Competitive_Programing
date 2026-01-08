H, W = map(int, input().split())
ans = H * W

if ans % 3 == 0:
	print(0)
	exit()

for h in range(1, H):
	a = h * W
	rem = H - h

	h2 = rem // 2
	b = h2 * W
	c = (rem - h2) * W
	ans = min(ans, max(a, b, c) - min(a, b, c))

	b = rem * (W // 2)
	c = rem * (W - W // 2)
	ans = min(ans, max(a, b, c) - min(a, b, c))

for w in range(1, W):
	a = H * w
	rem = W - w

	w2 = rem // 2
	b = H * w2
	c = H * (rem - w2)
	ans = min(ans, max(a, b, c) - min(a, b, c))

	b = (H // 2) * rem
	c = (H - H // 2) * rem
	ans = min(ans, max(a, b, c) - min(a, b, c))

print(ans)