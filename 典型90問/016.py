#016 - Minimum Coins（★3） 
N = int(input())
A, B, C = map(int, input().split())

ans = 10000
for i in range(min(10000, N // A + 1)):
	for j in range(min(10000 - i, (N - A*i) // B + 1)):
		rest = N - A * i - B * j
		if rest < 0:
			continue
		if rest % C != 0:
			continue
		k = rest // C
		if i + j + k <= 9999:
			ans = min(ans, i + j + k)

print(ans)