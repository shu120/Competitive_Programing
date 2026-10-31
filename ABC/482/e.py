# https://atcoder.jp/contests/typical90/submissions/72847867


def dfs(start, G, N):
    """DFS(stack): startからの距離と親を返す"""
    dist = [-1] * N
    parent = [-1] * N
    dist[start] = 0
    stack = [start]
    while stack:
        curr = stack.pop()
        for nxt in G[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                parent[nxt] = curr
                stack.append(nxt)
    return dist, parent


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

C = list(map(int, input().split()))

dist = dfs(0, G, N)
u = dist.index(max(dist))

dist_u, parent = dfs(u, G, N)
v = dist_u.index(max(dist_u))

dia = dist_u[v]

path = []
curr = v

while curr != -1:
    path.append(curr)
    curr = parent[curr]

path.reverse()

if dia % 2 == 0:
    center = path[dia // 2]
else:
    left = path[dia // 2]
    right = path[dia // 2 + 1]

# 木の頂点候補を調べる（入力例でいうところの(1,5)(3,5)）
# 色情報を入れる
