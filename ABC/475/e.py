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


N, M, K = map(int, input().split())
T = input()

A = []

for _ in range(N):
    S = input()
    x = 0
    for j in range(K):
        x <<= 1
        if S[j] == T[j]:
            x |= 1

    A.append(x)

Q = int(input())
queries = []

tmp = A.copy()
val = set(A)

for _ in range(Q):
    i, j = map(int, input().split())
    i -= 1
    j -= 1

    queries.append((i, j))

    tmp[i] ^= 1 << (K - 1 - j)
    val.add(tmp[i])

val = sorted(val)
idx = {x: i + 1 for i, x in enumerate(val)}

fw = Fenwick_Tree(len(val))

for x in A:
    fw.add(idx[x], 1)

for i, j in queries:
    fw.add(idx[A[i]], -1)
    A[i] ^= 1 << (K - 1 - j)

    fw.add(idx[A[i]], 1)

    lower = fw.sum(idx[A[i]] - 1)

    if A[i] != 0 and N - lower <= M:
        print("Yes")
    else:
        print("No")
