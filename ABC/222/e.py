# E - Red and Blue Tree
MOD = 998244353
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

G = [[] for _ in range(N)]
for edge in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, edge))
    G[v].append((u, edge))

C = [0] * (N - 1)

for i in range(M - 1):
    start = A[i]
    goal = A[i + 1]

    parent = [None] * N
    parent_edge = [None] * N

    parent[start] = start
    stack = [start]

    while stack:
        curr = stack.pop()
        if curr == goal:
            break
        for nxt, edge in G[curr]:
            if parent[nxt] is None:
                parent[nxt] = curr
                parent_edge[nxt] = edge
                stack.append(nxt)

    curr = goal

    while curr != start:
        edge = parent_edge[curr]
        C[edge] += 1
        curr = parent[curr]

S = sum(C)

if S + K < 0 or (S + K) % 2:
    print(0)
    exit()

X = (S + K) // 2

if X > S:
    print(0)
    exit()

dp = [0] * (X + 1)
dp[0] = 1

for c in C:
    ndp = [0] * (X + 1)

    for j in range(X + 1):
        ndp[j] += dp[j]
        ndp[j] %= MOD

        if j + c <= X:
            ndp[j + c] += dp[j]
            ndp[j + c] %= MOD

    dp = ndp

print(dp[X])
