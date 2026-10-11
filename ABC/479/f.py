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

    def range_sum(self, l, r):
        """[l, r] の和を返す"""
        return self.sum(r) - self.sum(l - 1)


def compress(A):
    """座標圧縮"""
    vals = sorted(set(A))
    comp = {v: i for i, v in enumerate(vals)}
    return [comp[x] for x in A]


N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

rank_S = compress(S)
rank_T = compress(T)

order_S = [0] * N
order_T = [0] * N

for i in range(N):
    order_S[rank_S[i]] = i

ans = 0

for i in range(N):
    s = S[i] - rank_S[i]
    t = T[i] - rank_T[i]

    ans += abs(s - t)

fw = Fenwick_Tree(N)

for i in range(N):
    p = order_S[i]
    r = rank_T[p] + 1

    ans += i - fw.sum(r)
    fw.add(r, 1)

print(ans)
