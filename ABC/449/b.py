import sys
input = sys.stdin.readline

H, W, Q = map(int, input().split())

for _ in range(Q):
	t, x = map(int, input().split())

	if t == 1:
		print(x * W)
		H -= x
	else:
		print(x * H)
		W -= x
