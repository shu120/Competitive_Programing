N, T = map(int, input().split())
dic = {}
for _ in range(N):
	c, t = map(int, input().split())
	dic[c] = t

ans = 1001

for cost, time in dic.items():
	if time <= T:
		ans = min(ans, cost)
if ans == 1001:
	print("TLE")
else:
	print(ans)