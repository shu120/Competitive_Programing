N = int(input())
H = list(map(int, input().split()))

mx = max(H)
mn = min(H)

if mn >= 0:
	print(2 * mx)
elif mx <= 0:
	print(-2 * mn)
else:
	print(2 * (mx - mn))