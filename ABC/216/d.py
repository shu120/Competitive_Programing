# D - Pair of Balls
from collections import deque

N, M = map(int, input().split())

tubes = []

for _ in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    tubes.append(a)

top = [[] for _ in range(N + 1)]
q = deque()

for i in range(M):
    c = tubes[i][-1]
    top[c].append(i)

    if len(top[c]) == 2:
        q.append(c)

cnt = 0

while q:
    c = q.popleft()

    for i in top[c]:
        tubes[i].pop()
        cnt += 1

        if tubes[i]:
            nxt = tubes[i][-1]
            top[nxt].append(i)

            if len(top[nxt]) == 2:
                q.append(nxt)

print("Yes" if cnt == 2 * N else "No")
