# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py

from collections import deque
from heapq import heappop, heappush


def compress(A):
    """座標圧縮"""
    vals = sorted(set(A))
    comp = {v: i for i, v in enumerate(vals)}
    return [comp[x] for x in A]


def dfs(start, G, N):
    """DFS(stack): startからのDFS木上の深さを返す（未訪問は-1）"""
    dist = [-1] * N
    dist[start] = 0
    stack = [start]

    while stack:
        curr = stack.pop()

        for nxt in G[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                stack.append(nxt)

    return dist


def bfs(start, G, N):
    """BFS(queue): startからの各頂点への最短距離を返す（到達不能は-1）"""
    dist = [-1] * N
    dist[start] = 0
    q = deque([start])

    while q:
        curr = q.popleft()

        for nxt in G[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)

    return dist


def dijkstra(G, start):
    """Dijkstra法"""
    N = len(G)
    inf = 1 << 62
    dist = [inf] * N
    dist[start] = 0
    q = [(0, start)]

    while q:
        dv, v = heappop(q)

        if dist[v] != dv:
            continue

        for u, cost in G[v]:
            du = dv + cost

            if du < dist[u]:
                dist[u] = du
                heappush(q, (du, u))

    return dist


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


class Fenwick_Tree:
    """Fenwick Tree (BIT)
    1-indexed / 点更新・前方和クエリ
    """

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        """i番目に v を加算"""
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        """[1, i] の和を返す"""
        s = 0

        while i > 0:
            s += self.bit[i]
            i -= i & -i

        return s

    def range_sum(self, left, right):
        """[left, right] の和を返す"""
        return self.sum(right) - self.sum(left - 1)


class UnionFind:
    """Union-Find（Disjoint Set Union）
    0-indexed / 連結判定・サイズ管理
    """

    def __init__(self, n):
        """n 要素の Union-Find を初期化"""
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        """x が属する集合の根を返す"""
        if self.par[x] == -1:
            return x

        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def issame(self, x, y):
        """x と y が同じ集合に属するか判定"""
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        """x と y の属する集合を併合する（成功時 True）"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            x, y = y, x

        self.par[y] = x
        self.siz[x] += self.siz[y]

        return True

    def size(self, x):
        """x が属する集合の要素数を返す"""
        return self.siz[self.root(x)]


class SegTree:
    """Segment Tree
    0-indexed / 点更新・区間クエリ

    Parameters
    ----------
    A : list
        初期配列
    op : function
        2つの区間情報を結合する関数
    e : any
        opの単位元

    Methods
    -------
    update(i, x)
        A[i] を x に変更する
    query(left, right)
        閉区間 [left, right] の情報を取得する
    all_query()
        配列全体の情報を取得する
    """

    def __init__(self, A, op, e):
        self.op = op
        self.e = e
        self.n = len(A)

        self.size = 1

        while self.size < self.n:
            self.size <<= 1

        self.data = [e] * (2 * self.size)

        for i in range(self.n):
            self.data[self.size + i] = A[i]

        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def update(self, i, x):
        """A[i] を x に変更する"""
        i += self.size
        self.data[i] = x

        while i > 1:
            i >>= 1
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def query(self, left, right):
        """閉区間 [left, right] の情報を取得する"""
        left += self.size
        right += self.size

        res_left = self.e
        res_right = self.e

        while left <= right:
            if left & 1:
                res_left = self.op(
                    res_left,
                    self.data[left]
                )
                left += 1

            if not (right & 1):
                res_right = self.op(
                    self.data[right],
                    res_right
                )
                right -= 1

            left >>= 1
            right >>= 1

        return self.op(res_left, res_right)

    def all_query(self):
        """配列全体の情報を取得する"""
        return self.data[1]

