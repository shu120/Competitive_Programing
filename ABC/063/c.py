N = int(input())
S = [int(input()) for _ in range(N)]

total = sum(S)

if total % 10 != 0:
	print(total)
else:
	others = [s for s in S if s % 10 != 0]
	if others:
		print(total - min(others))
	else:
		print(0)