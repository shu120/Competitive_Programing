N = int(input())
S = [input() for _ in range(N)]

m = 0
for s in S:
	if len(s) > m:
		m = len(s)
		
for s in S:
	k = (m - len(s)) // 2
	print("." * k + s + "." * k)