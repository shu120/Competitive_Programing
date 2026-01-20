#D - joisino's travel
import sys
input = sys.stdin.readline
from itertools import permutations

INF = 10**18

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
r = [x - 1 for x in r]

dist = [[INF] * N for _ in range(N)]
for i in range(N):
	dist[i][i] = 0

for _ in range(M):
	A, B, C = map(int, input().split())
	A -= 1
	B -= 1
	if C < dist[A][B]:
		dist[A][B] = C
		dist[B][A] = C

for k in range(N):
	dk = dist[k]
	for i in range(N):
		di = dist[i]
		aik = di[k]
		if aik == INF:
			continue
		for j in range(N):
			v = aik + dk[j]
			if v < di[j]:
				di[j] = v

ans = INF
for order in permutations(r):
	s = 0
	for i in range(R - 1):
		s += dist[order[i]][order[i + 1]]
	if s < ans:
		ans = s

print(ans)