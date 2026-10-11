import sys
input = sys.stdin.readline

N = int(input())

x = []

G = [[] for _ in range(N)]
edge = []
for i in range(1, N):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
    edge.append((A, B))

parent = [-1] * N
order = [0]

for v in order:
    for nv in G[v]:
        if nv == parent[v]:
            continue

        parent[nv] = v
        order.append(nv)

size = [1] * N

for v in reversed(order):
    if parent[v] != -1:
        size[parent[v]] += size[v]

add = [0] * N
total = 0

for i, (A, B) in enumerate(edge, 1):
    if parent[A] == B:
        child = A
    else:
        child = B

    if size[child] * 2 > N:
        add[child] += i

    else:
        total += i
        add[child] -= i

for v in order:
    if parent[v] != -1:
        add[v] += add[parent[v]]

for i in range(N):
    x.append(total + add[i])

print(*x)
