import sys
input = sys.stdin.readline

N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))

if max(W) > max(C):
	print("No")
	exit()

if sum(W) > sum(C):
	print("No")
	exit()

W.sort(reverse=True)

loads = [0] * M

def dfs(i):
	if i == N:
		return True

	w = W[i]

	order = sorted(range(M), key=lambda j: C[j] - loads[j], reverse=True)

	for j in order:
		if loads[j] + w <= C[j]:
			loads[j] += w
			if dfs(i + 1):
				return True
			loads[j] -= w

	return False

print("Yes" if dfs(0) else "No")