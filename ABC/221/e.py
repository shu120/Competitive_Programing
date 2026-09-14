# E - LEQ
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

val = sorted(set(A))
idx = {x: i + 1 for i, x in enumerate(val)}


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

    def range_sum(self, _l, r):
        """[l, r] の和を返す"""
        return self.sum(r) - self.sum(_l - 1)


fw = Fenwick_Tree(len(val))

inv2 = pow(2, MOD - 2, MOD)

ans = 0
pow2 = 1
invpow2 = inv2

for j in range(N):
    p = idx[A[j]]

    s = fw.sum(p)

    ans += pow2 * s
    ans %= MOD

    fw.add(p, invpow2)

    pow2 = pow2 * 2 % MOD
    invpow2 = invpow2 * inv2 % MOD

print(ans)
