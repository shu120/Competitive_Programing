#C
s = input()

n = len(s)
pair =[]
cnt = 1
for i in range(1, n):
	if s[i] == s[i - 1]:
		cnt += 1
	else:
		pair.append((int(s[i - 1]), cnt))
		cnt = 1
pair.append((int(s[n - 1]), cnt))

ans = 0

for i in range(len(pair) - 1):
	x, nx = pair[i]
	y, ny = pair[i + 1]
	if y == x + 1:
		ans += min(nx, ny)

print(ans)