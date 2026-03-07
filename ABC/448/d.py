import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def compress(A):
	"""座標圧縮"""
	vals = sorted(set(A))
	comp = {v:i for i,v in enumerate(vals)}
	return [comp[x] for x in A]

A = compress(A)
cnt = [0] * N

G = [[] for _ in range(N)]
for _ in range(N - 1):
	u, v = map(int,input().split())
	u -= 1
	v -= 1
	G[u].append(v)
	G[v].append(u)

ans = [False] * N

def dfs(v, parent, dup):

	cnt[A[v]] += 1
	if cnt[A[v]] == 2:
		dup = True

	ans[v] = dup

	for nv in G[v]:
		if nv == parent:
			continue
		dfs(nv, v, dup)

	cnt[A[v]] -= 1

dfs(0, -1, False)

for x in ans:
	print("Yes" if x else "No")