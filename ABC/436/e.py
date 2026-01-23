#E
N = int(input())
P = [0] + list(map(int, input().split()))

visited = [False] * (N + 1)
ans = 0

for i in range (1, N + 1):
	if visited[i]:
		continue
	curr = i
	length = 0
	while not visited[curr]:
		visited[curr] = True
		length += 1
		curr = P[curr]
	ans += length * (length - 1) // 2
print(ans)