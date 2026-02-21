import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M, A, B = map(int, input().split())

state = [[0] * M for _ in range(M)]

def dfs(a, b):
	if a % M == 0:
		return False
	
	if state[a][b] == 2:
		return True
	if state[a][b] == 3:
		return False
	if state[a][b] == 1:
		return True
	
	state[a][b] = 1
	
	na = b
	nb = (A * b + B * a) % M
	
	ok = dfs(na, nb)
	
	if ok:
		state[a][b] = 2
	else:
		state[a][b] = 3
	
	return ok

ans = 0

for x in range(M):
	for y in range(M):
		if dfs(x, y):
			ans += 1

print(ans)