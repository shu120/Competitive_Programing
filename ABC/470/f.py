from collections import defaultdict


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


N, M = map(int, input().split())
S = input()
MOD = 998244353

uf = UnionFind(N)

for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    uf.unite(A, B)

fact = [1] * (N + 1)
inv_fact = [1] * (N + 1)

for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[N] = pow(fact[N], MOD - 2, MOD)

for i in range(N, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD

cnt = defaultdict(int)

for i, c in enumerate(S):
    r = uf.root(i)
    cnt[(r, c)] += 1

ways = 1
dup = False

for i in range(N):
    if uf.root(i) == i:
        ways *= fact[uf.size(i)]
        ways %= MOD

for num in cnt.values():
    ways *= inv_fact[num]
    ways %= MOD

    if num >= 2:
        dup = True

if dup:
    ans = ways
else:
    ans = ways * pow(2, MOD - 2, MOD) % MOD

print(ans)
