#B
import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
	for j in range(i+1, n):
		dis = sum((x[i][k] - x[j][k])** 2 for k in range(d))
		if math.sqrt(dis) == int(math.sqrt(dis)):
			ans += 1
print(ans)