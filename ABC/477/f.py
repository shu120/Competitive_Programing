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


N, M, Q = map(int, input().split())

L = [0] * N
R = [0] * N

for i in range(N):
    L[i], R[i] = map(int, input().split())

events = [[] for _ in range(N + 1)]
ans = [0] * Q

for i in range(Q):
    A, B, C, D = map(int, input().split())

    events[B].append((C, D, i, 1))
    events[A - 1].append((C, D, i, -1))

bit_a = Fenwick_Tree(M + 1)
bit_b = Fenwick_Tree(M + 1)


def range_add(bit, left, right, value):
    if left > right:
        return

    bit.add(left, value)
    bit.add(right + 1, -value)


def get(x):
    if x <= 0:
        return 0

    a = bit_a.sum(x)
    b = bit_b.sum(x)

    return a * x + b


for row in range(N + 1):
    if row > 0:
        left = L[row - 1]
        right = R[row - 1]

        range_add(bit_a, left, right, 1)
        range_add(bit_b, left, right, 1 - left)

        if right < M:
            range_add(bit_b, right + 1, M, right - left + 1)

    for C, D, idx, sign in events[row]:
        ans[idx] += sign * (get(D) - get(C - 1))

for x in ans:
    print(x)
