N, S, T = map(int, input().split())
A = list(map(int, input().split()))

time = 60 * (T - S)
if sum(A) <= time:
	print("Yes")
else:
	print("No")