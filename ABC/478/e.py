# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py
import sys
input = sys.stdin.readline


class SCC:
    """Strongly Connected Components.

    0-indexed / 強連結成分分解
    """

    def __init__(self, n):
        """n 頂点の有向グラフを初期化する。"""
        self.n = n
        self.G = [[] for _ in range(n)]
        self.rev_G = [[] for _ in range(n)]

    def add_edge(self, u, v):
        """有向辺 u -> v を追加する。"""
        self.G[u].append(v)
        self.rev_G[v].append(u)

    def scc(self):
        """強連結成分と各頂点の成分番号を返す。"""
        used = [False] * self.n
        order = []

        for start in range(self.n):
            if used[start]:
                continue

            used[start] = True
            stack = [(start, 0)]

            while stack:
                curr, idx = stack[-1]

                if idx < len(self.G[curr]):
                    nxt = self.G[curr][idx]
                    stack[-1] = (curr, idx + 1)

                    if not used[nxt]:
                        used[nxt] = True
                        stack.append((nxt, 0))
                else:
                    order.append(curr)
                    stack.pop()

        group_id = [-1] * self.n
        groups = []

        for start in reversed(order):
            if group_id[start] != -1:
                continue

            idx = len(groups)
            group = []
            stack = [start]
            group_id[start] = idx

            while stack:
                curr = stack.pop()
                group.append(curr)

                for nxt in self.rev_G[curr]:
                    if group_id[nxt] == -1:
                        group_id[nxt] = idx
                        stack.append(nxt)

            groups.append(group)

        return groups, group_id


N, Q = map(int, input().split())

scc = SCC(N)
query = []

for _ in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1

    scc.add_edge(u, v)
    query.append((t, u, v))

groups, group_id = scc.scc()

for t, u, v in query:
    if t == 1 and group_id[u] == group_id[v]:
        print("No")
        exit()

A = [0] * N

for i in range(N):
    A[i] = group_id[i] + 1

print("Yes")
print(*A)
