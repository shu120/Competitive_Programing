n, m = map(int, input().split())
conds = []
for _ in range(m):
	s, c = map(int, input().split())
	conds.append((s, c))
ans = -1

for i in range (10 ** n):
	si = str(i)
	if len(si) < n:
		si = '0' * (n - len(si)) + si
	if n >= 2 and si[0] == '0':
		continue
	ok = True
	for (s, c) in conds:
		if int(si[s - 1]) != c:
			ok = False
			break
	if ok:
		ans = si
		break
print(ans)