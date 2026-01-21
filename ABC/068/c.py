#ABC068 C - Cat Snuke and a Voyage
N, M = map(int, input().split())
adj = [set() for _ in range(N)]

for _ in range(M):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	adj[a].add(b)
	adj[b].add(a)

if adj[0] & adj[N-1]:
	print("POSSIBLE")
else:
	print("IMPOSSIBLE")