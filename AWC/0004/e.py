import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = {0: 1}
s = 0
ans = 0

for a in A:
	s += a
	
	if s - K in cnt:
		ans += cnt[s - K]
	
	if s in cnt:
		cnt[s] += 1
	else:
		cnt[s] = 1

print(ans)