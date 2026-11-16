# F - Colorful Tree
# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py
import sys
input = sys.stdin.readline


class LCA:
    """ダブリングで木の最小共通祖先（Lowest Common Ancestor）と頂点間距離を求める。

    仕様:
        頂点番号は 0 始まり。空でない連結な木を、指定した root を根として扱う。
        query(u, v) で共通祖先のうち最も深い頂点、dist(u, v) で経路の辺数を得る。
        自分自身も祖先に含める。構築後の辺の追加・削除や根の変更には対応しない。
        木であることや頂点番号の範囲チェックは行わない。
    Order:
        頂点数を N として前処理は時間・領域 O(N log N)。
        最小共通祖先・距離の取得は時間 O(log N)。
    使用例:
        tree = LCA([[1], [0, 2, 3], [1], [1]])
        tree.query(2, 3)  # 1
        tree.dist(2, 3)  # 2
    """

    def __init__(self, G, root=0):
        """根からの深さと、2 の累乗個だけ上の祖先を前計算する。

        Parameter:
            G: 重みなしの無向木の隣接リスト。頂点数は 1 以上。
                辺 u-v は G[u] と G[v] の両方に格納する。
            root: 根の頂点番号。0 <= root < len(G)。省略時は 0。
        Return:
            None。depth[v] に根からの深さ（辺数）、parent[k][v] に
            v の 2**k 個上の祖先を格納する。存在しない祖先は -1。
            G は変更しない。探索はスタックを使い、再帰は使わない。
        Order:
            N = len(G) として時間 O(N log N)、領域 O(N log N)。
        """
        self.n = len(G)
        self.log = self.n.bit_length()

        self.depth = [-1] * self.n
        self.parent = [[-1] * self.n for _ in range(self.log)]

        self.depth[root] = 0
        stack = [root]

        while stack:
            curr = stack.pop()

            for nxt in G[curr]:
                if self.depth[nxt] != -1:
                    continue

                self.depth[nxt] = self.depth[curr] + 1
                self.parent[0][nxt] = curr
                stack.append(nxt)

        for k in range(1, self.log):
            for v in range(self.n):
                p = self.parent[k - 1][v]

                if p != -1:
                    self.parent[k][v] = self.parent[k - 1][p]

    def query(self, u, v):
        """2 頂点の最小共通祖先を取得する。

        Parameter:
            u, v: 頂点番号。いずれも 0 以上 self.n 未満。
        Return:
            構築時に指定した根に対する最小共通祖先の頂点番号。
            u == v ならその頂点、一方が他方の祖先なら祖先側の頂点を返す。
        Order:
            時間 O(log N)、追加領域 O(1)。N は頂点数。
        """
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]

        for k in range(self.log):
            if diff >> k & 1:
                u = self.parent[k][u]

        if u == v:
            return u

        for k in range(self.log - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]

    def dist(self, u, v):
        """2 頂点を結ぶ一意な経路の辺数を取得する。

        Parameter:
            u, v: 頂点番号。いずれも 0 以上 self.n 未満。
        Return:
            u から v までの距離（辺数）。u == v のときは 0。
            重み付きの距離や、経路上の頂点数ではない。
        Order:
            時間 O(log N)、追加領域 O(1)。N は頂点数。
        """
        w = self.query(u, v)

        return (self.depth[u] + self.depth[v] - 2 * self.depth[w])


N, Q = map(int, input().split())

G = [[] for _ in range(N)]
G_lca = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c, d))
    G[b].append((a, c, d))
    G_lca[a].append(b)
    G_lca[b].append(a)

tree = LCA(G_lca)

parent = [-1] * N
parent[0] = 0
dist = [0] * N
stack = [0]

while stack:
    curr = stack.pop()

    for nxt, color, length in G[curr]:
        if parent[nxt] != -1:
            continue

        parent[nxt] = curr
        dist[nxt] = dist[curr] + length
        stack.append(nxt)

q = []
bfr_dist = [0] * Q
event = [[] for _ in range(N)]

for i in range(Q):
    x, y, u, v = map(int, input().split())
    u -= 1
    v -= 1

    lca = tree.query(u, v)
    bfr_dist[i] = dist[u] + dist[v] - 2 * dist[lca]

    q.append((x, y))

    # root→u + root→v - 2×root→lcaの係数
    event[u].append((i, x, 1))
    event[v].append((i, x, 1))
    event[lca].append((i, x, -2))

q_cnt = [0] * Q
q_sum = [0] * Q

cnt = [0] * (N + 1)
tot = [0] * (N + 1)

stack = [(0, -1, 0, 0, 0)]

while stack:
    curr, par, color, leng, state = stack.pop()

    if state == 0:
        if par != -1:
            cnt[color] += 1
            tot[color] += leng

        for i, x, coef in event[curr]:
            q_cnt[i] += coef * cnt[x]
            q_sum[i] += coef * tot[x]

        stack.append((curr, par, color, leng, 1))

        for nxt, nxt_color, nxt_leng in G[curr]:
            if nxt == par:
                continue

            stack.append((nxt, curr, nxt_color, nxt_leng, 0))

    else:
        if par != -1:
            cnt[color] -= 1
            tot[color] -= leng

for i in range(Q):
    x, y = q[i]

    ans = bfr_dist[i]
    ans -= q_sum[i]
    ans += q_cnt[i] * y

    print(ans)
