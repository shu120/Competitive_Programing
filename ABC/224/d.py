# D - 8 Puzzle on Graph
from collections import deque

M = int(input())

G = [[] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    G[u].append(v)
    G[v].append(u)

p = list(map(int, input().split()))

start = [8] * 9

for i in range(8):
    start[p[i] - 1] = i

start = tuple(start)
goal = tuple(range(9))

dist = {start: 0}
q = deque([start])

while q:
    curr = q.popleft()

    if curr == goal:
        print(dist[curr])
        exit()

    empty = curr.index(8)

    for nxt in G[empty]:
        state = list(curr)
        state[empty], state[nxt] = state[nxt], state[empty]
        state = tuple(state)

        if state not in dist:
            dist[state] = dist[curr] + 1
            q.append(state)

print(-1)
