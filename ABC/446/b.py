N, M = map(int, input().split())

used = set()
ans = []

for _ in range(N):
	L = int(input())
	wishes = list(map(int, input().split()))
	
	chosen = 0
	for x in wishes:
		if x not in used:
			chosen = x
			used.add(x)
			break
	
	ans.append(chosen)

for x in ans:
	print(x)