import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(M)]

color = [0] * (N + 1)
parent = list(range(N + 2))


def find(x: int) -> int:
    root = x
    while parent[root] != root:
        root = parent[root]

    while parent[x] != x:
        nxt = parent[x]
        parent[x] = root
        x = nxt

    return root


for left, right, paint in reversed(queries):
    pos = find(left)
    while pos <= right:
        color[pos] = paint
        parent[pos] = find(pos + 1)
        pos = find(pos)

print(*color[1:])
