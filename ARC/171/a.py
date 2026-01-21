import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, A, B = map(int, input().split())

	if A > N:
		print("No")
		continue
	if A <= N // 2:
		maxB = (N - A) * ((N + 1) // 2)
	else:
		maxB = (N - A) ** 2
	
	print("Yes" if B <= maxB else "No")