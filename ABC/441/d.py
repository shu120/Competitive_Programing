#D - Paid Walk
import sys
input = sys.stdin.readline

N, M, L, S, T = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for _ in range(M):
	U, V, C = map(int, input().split())
	adj[U].append((V, C))

ok = [False] * (N + 1)

stack = [(1, 0, 0)]

while stack:
	V, steps, cost = stack.pop()

	if steps == L:
		if S <= cost <= T:
			ok[V] = True
		continue
	for to, w in adj[V]:
		nex = cost + w
		if nex <= T:
			stack.append((to, steps + 1, nex))

ans = []
for i in range(1, N + 1):
	if ok[i]:
		ans.append(i)

if len(ans) == 0:
	print()
else:
	print(*ans)
