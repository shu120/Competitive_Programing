# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py

from collections import deque
from heapq import heappop, heappush


def sort_cmp(data, cmp):
    """cmp_to_key を使わず、比較関数 cmp で安定マージソートで直接並べ替える。

    Parameter:
        data: 並べ替えるリスト。空リストも受け付ける。
        cmp: a を b より前に置くとき cmp(a, b) が True になる関数。
            同順位では False を返し、比較の順序に矛盾がないようにする。
    Return:
        None。data 自体を更新し、同順位の要素の元の順序を保つ。
    Order:
        要素数を N として時間 O(N log N)、追加領域 O(N)。比較は O(1) とする。
    使用例:
        sort(data, lambda a, b: a < b)  # 昇順（降順は a > b）
    """
    n = len(data)
    if n <= 1:
        return

    src = data[:]
    dst = [None] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            i, j = left, mid

            for k in range(left, right):
                if i < mid and (j == right or not cmp(src[j], src[i])):
                    dst[k] = src[i]
                    i += 1
                else:
                    dst[k] = src[j]
                    j += 1

        src, dst = dst, src
        width *= 2

    data[:] = src


def compress(A):
    """値の大小関係を保ったまま、配列を 0 始まりの連続した整数に変換する。

    Parameter:
        A: 要素同士を大小比較でき、set・dict のキーとして使える値の配列。
    Return:
        各要素を昇順での順位に置き換えた新しいリスト。同じ値は同じ順位になる。
        A は変更せず、空配列には空リストを返す。
    Order:
        要素数を N、異なる値の数を K として時間 O(N + K log K)、追加領域 O(N + K)。
        ハッシュ操作は平均 O(1)、値の比較は O(1) とする。
    使用例:
        compress([30, 10, 30, 20])  # [2, 0, 2, 1]
    """
    vals = sorted(set(A))
    comp = {v: i for i, v in enumerate(vals)}
    return [comp[x] for x in A]


def dfs(start, G, N):
    """スタックを使ってグラフを探索し、発見時の親から数えた深さを求める。

    Parameter:
        start: 始点の頂点番号。0 <= start < N。
        G: 隣接リスト。G[v] に頂点 v から移動できる頂点番号を格納する。
        N: 頂点数。頂点番号は 0 から N - 1。有向・無向の両方に対応する。
    Return:
        長さ N のリスト。始点は 0、到達不能な頂点は -1。
        頂点をスタックに積む時点で訪問済みにするため、深さは隣接リストの順序に
        依存し、一般のグラフでは最短距離や再帰 DFS の深さとは一致しない。
    Order:
        辺数（隣接リストの総要素数）を M として時間 O(N + M)、追加領域 O(N)。
    """
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
    """幅優先探索で、始点から各頂点までの最小移動回数を求める。

    Parameter:
        start: 始点の頂点番号。0 <= start < N。
        G: 隣接リスト。G[v] に頂点 v から移動できる頂点番号を格納する。
        N: 頂点数。頂点番号は 0 から N - 1。有向・無向の両方に対応する。
    Return:
        長さ N の最短距離リスト。始点は 0、到達不能な頂点は -1。
        各辺の移動コストを 1 として扱う。
    Order:
        辺数（隣接リストの総要素数）を M として時間 O(N + M)、追加領域 O(N)。
    """
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
    """Dijkstra 法で、非負の辺重みを持つグラフの単一始点最短距離を求める。

    Parameter:
        G: 重み付き隣接リスト。G[v] に (移動先の頂点番号, コスト) を格納する。
            頂点番号は 0 から len(G) - 1。すべてのコストは 0 以上とする。
        start: 始点の頂点番号。0 <= start < len(G)。
    Return:
        各頂点までの最小コストを格納したリスト。始点は 0、到達不能は 1 << 62。
        到達可能な頂点の最短距離は 1 << 62 未満である必要がある。
    Order:
        頂点数を N、辺数（隣接リストの総要素数）を M として
        時間 O(N + M log(M + 1))、追加領域 O(N + M)。重複辺も許容する。
    """
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
    """有向グラフを、互いに行き来できる頂点の集合（強連結成分）に分解する。

    仕様:
        頂点番号は 0 始まり。add_edge(u, v) で辺を追加し、scc() で分解する。
        正方向・逆方向の隣接リストを持ち、再帰を使わない Kosaraju 法で探索する。
    Order:
        頂点数を N、辺数を M として、グラフの保持に O(N + M) の領域を使う。
        初期化は O(N)、辺追加は償却 O(1)、分解は O(N + M) 時間。
    """

    def __init__(self, n):
        """辺を持たない有向グラフを初期化する。

        Parameter:
            n: 頂点数（0 以上）。頂点番号は 0 から n - 1。
        Return:
            None。正方向・逆方向の隣接リストを作成する。
        Order:
            時間 O(n)、領域 O(n)。
        """
        self.n = n
        self.G = [[] for _ in range(n)]
        self.rev_G = [[] for _ in range(n)]

    def add_edge(self, u, v):
        """有向辺 u -> v を追加する。

        Parameter:
            u: 辺の始点。0 <= u < self.n。
            v: 辺の終点。0 <= v < self.n。自己ループ・重複辺も追加できる。
        Return:
            None。正方向・逆方向の隣接リストを更新する。
        Order:
            償却時間 O(1)、追加領域 O(1)。
        """
        self.G[u].append(v)
        self.rev_G[v].append(u)

    def scc(self):
        """現在のグラフを強連結成分に分解する。

        Parameter:
            なし。
        Return:
            (groups, group_id) のタプル。
            groups[i] は成分 i に属する頂点番号のリスト。
            group_id[v] は頂点 v の成分番号（0 始まり）。
            異なる成分を結ぶ辺 u -> v では group_id[u] < group_id[v] となる。
            成分内の頂点順序は保証しない。空グラフには ([], []) を返す。
        Order:
            頂点数を N、辺数を M として時間 O(N + M)、追加領域 O(N)。
        """
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
    """配列の一点への加算と区間和の取得を行う Fenwick Tree（BIT）。

    仕様:
        添字は 1 始まり。初期値はすべて 0。
        add(i, v) で加算し、sum(i) で前方和、range_sum(left, right) で区間和を得る。
        区間は両端を含む。添字の範囲チェックは行わない。
    Order:
        要素数を N として初期化は時間・領域 O(N)。各操作は時間 O(log N)。
    """

    def __init__(self, n):
        """全要素が 0 の配列を管理する BIT を初期化する。

        Parameter:
            n: 要素数（0 以上）。使用する添字は 1 から n。
        Return:
            None。長さ n + 1 の内部配列を作成する。
        Order:
            時間 O(n)、領域 O(n)。
        """
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        """指定した要素に値を加算する。

        Parameter:
            i: 更新する添字。1 <= i <= self.n。0 は指定しない。
            v: 加算する値。負の値を指定すると減算になる。
        Return:
            None。管理する配列の i 番目の値を v だけ増やす。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        """閉区間 [1, i] の和を取得する。

        Parameter:
            i: 区間の右端。0 <= i <= self.n。
        Return:
            1 番目から i 番目までの合計。i = 0 のときは 0。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        s = 0

        while i > 0:
            s += self.bit[i]
            i -= i & -i

        return s

    def range_sum(self, left, right):
        """両端を含む指定区間の和を取得する。

        Parameter:
            left: 区間の左端。1 <= left <= right。
            right: 区間の右端。right <= self.n。
        Return:
            閉区間 [left, right] の合計。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        return self.sum(right) - self.sum(left - 1)


class UnionFind:
    """要素を互いに素な集合に分け、集合の併合・連結判定・サイズ取得を行う。

    仕様:
        要素番号は 0 始まり。初期状態では各要素が別々の集合に属する。
        経路圧縮とサイズによる併合を使う。要素の削除や集合の分割には対応しない。
    Order:
        要素数を N として初期化は時間・領域 O(N)。
        各操作は償却時間 O(α(N))。α は逆 Ackermann 関数で、実用上ほぼ定数。
    """

    def __init__(self, n):
        """各要素が単独の集合に属する Union-Find を初期化する。

        Parameter:
            n: 要素数（0 以上）。要素番号は 0 から n - 1。
        Return:
            None。親と集合サイズを管理する内部配列を作成する。
        Order:
            時間 O(n)、領域 O(n)。
        """
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        """要素が属する集合の代表元を取得し、探索経路を圧縮する。

        Parameter:
            x: 要素番号。0 <= x < len(self.par)。
        Return:
            x が属する集合の代表元の番号。併合によって代表元は変わることがある。
        Order:
            償却時間 O(α(N))、再帰による追加領域は最悪 O(log N)。N は要素数。
        """
        if self.par[x] == -1:
            return x

        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def issame(self, x, y):
        """2 つの要素が同じ集合に属するか判定する。

        Parameter:
            x, y: 要素番号。いずれも 0 以上 len(self.par) 未満。
        Return:
            同じ集合に属するなら True、異なる集合なら False。
        Order:
            償却時間 O(α(N))、追加領域は最悪 O(log N)。N は要素数。
        """
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        """2 つの要素が属する集合を、サイズの大きい集合にまとめる。

        Parameter:
            x, y: 要素番号。いずれも 0 以上 len(self.par) 未満。
        Return:
            異なる集合を併合した場合は True、すでに同じ集合なら False。
            併合後は代表元の親情報と集合サイズを更新する。
        Order:
            償却時間 O(α(N))、追加領域は最悪 O(log N)。N は要素数。
        """
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
        """指定した要素が属する集合の要素数を取得する。

        Parameter:
            x: 要素番号。0 <= x < len(self.par)。
        Return:
            x 自身を含む集合の要素数。
        Order:
            償却時間 O(α(N))、追加領域は最悪 O(log N)。N は要素数。
        """
        return self.siz[self.root(x)]


class SegTree:
    """配列の一点更新と、結合則を満たす演算による区間集約を行う Segment Tree。

    仕様:
        添字は 0 始まり。query(left, right) は両端を含む閉区間を扱う。
        op は結合則 op(op(a, b), c) == op(a, op(b, c)) を満たす必要がある。
        e は op(e, x) == op(x, e) == x を満たす単位元。可換性は不要。
        op は引数を破壊せず、e は変更せずに使う。添字の範囲チェックは行わない。
    Order:
        要素数を N として初期化は時間・領域 O(N)。
        点更新・区間取得は時間 O(log N)、全体取得は O(1)。op は O(1) とする。
    使用例:
        seg = SegTree([1, 2, 3], lambda a, b: a + b, 0)
        seg.query(0, 1)  # 3
    """

    def __init__(self, A, op, e):
        """初期配列と集約演算からセグメント木を構築する。

        Parameter:
            A: 初期配列。空配列も指定できる。
            op: 2 つの値を結合する関数。結合則を満たす必要がある。
            e: op の単位元。例として、和なら 0、最大値なら float('-inf')。
        Return:
            None。A の要素を内部配列へ格納する。以後の update は A を更新しない。
        Order:
            N = len(A) として時間 O(N)、領域 O(N)。op は O(1) とする。
        """
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
        """指定した要素を新しい値に置き換える。

        Parameter:
            i: 更新する添字。0 <= i < self.n。
            x: 更新後の値。op で結合できる値を指定する。
        Return:
            None。内部の i 番目の要素と、その要素を含む区間の集約値を更新する。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数、op は O(1) とする。
        """
        i += self.size
        self.data[i] = x

        while i > 1:
            i >>= 1
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def query(self, left, right):
        """両端を含む指定区間を、左から右の順序で集約する。

        Parameter:
            left: 区間の左端。通常は 0 <= left <= right。
            right: 区間の右端。通常は right < self.n。
                空区間は 0 <= left <= self.n、-1 <= right < self.n、left > right とする。
        Return:
            閉区間 [left, right] の要素を op で結合した値。空区間には e を返す。
            文字列結合など、左右の順序で結果が変わる演算も利用できる。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数、op は O(1) とする。
        """
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
        """管理する配列全体の集約値を取得する。

        Parameter:
            なし。
        Return:
            全要素を左から右の順序で op により結合した値。空配列には e を返す。
        Order:
            時間 O(1)、追加領域 O(1)。
        """
        return self.data[1]
