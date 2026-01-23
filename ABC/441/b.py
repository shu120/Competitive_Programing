#B - Two Languages
N, M = map(int, input().split())
S = set(input())
T = set(input())
Q = int(input())
for _ in range(Q):
	w = input()

	inS = True
	inT = True

	for c in w:
		if c not in S:
			inS = False
		if c not in T:
			inT = False

	if inS and not inT:
		print("Takahashi")
	elif inT and not inS:
		print("Aoki")
	else:
		print("Unknown")