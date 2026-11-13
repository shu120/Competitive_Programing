# E - Just one
# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py

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


MOD = 998244353
N, M = map(int, input().split())

uf = UnionFind(N)
edges = []

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.unite(u, v)
    edges.append((u, v))

edge = [0] * N
ans = 1

for u, v in edges:
    root = uf.root(u)
    edge[root] += 1

for i in range(N):
    if uf.root(i) != i:
        continue

    if uf.size(i) != edge[i]:
        print(0)
        exit()

    ans = ans * 2 % MOD

print(ans)
