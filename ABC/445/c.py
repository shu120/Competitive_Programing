N = int(input())
A = [0] + list(map(int, input().split()))

visited = [0] * (N + 1)
ans = [0] * (N + 1)

def process(start):
	path = []
	cur = start

	while not visited[cur]:
		visited[cur] = start
		path.append(cur)
		cur = A[cur]

	if visited[cur] == start:
		idx = path.index(cur)
		cycle = path[idx:]
		L = len(cycle)

		K = pow(10, 100, L)

		for j, v in enumerate(cycle):
			ans[v] = cycle[(j + K) % L]

	for v in reversed(path):
		if ans[v]:
			continue
		ans[v] = ans[A[v]]

for i in range(1, N + 1):
	if not visited[i]:
		process(i)

print(*ans[1:])