from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
H = list(map(int, input().split()))

maxdq = deque()
mindq = deque()
ans = 0

for r in range(N):
	while maxdq and H[maxdq[-1]] <= H[r]:
		maxdq.pop()
	maxdq.append(r)

	while mindq and H[mindq[-1]] >= H[r]:
		mindq.pop()
	mindq.append(r)

	if maxdq[0] <= r - K:
		maxdq.popleft()
	if mindq[0] <= r - K:
		mindq.popleft()

	if r >= K - 1:
		ans = max(ans, H[maxdq[0]] - H[mindq[0]])

print(ans)