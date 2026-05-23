import sys
input = sys.stdin.readline


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
        i = min(i, self.n)

        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


N, Q = map(int, input().split())

height = [0] * N
base = 0

fw = Fenwick_Tree(Q + 2)
fw.add(1, N)

ans = []

for _ in range(Q):
    t, v = map(int, input().split())
    if t == 1:
        x = v - 1

        old = height[x]
        fw.add(old + 1, -1)

        height[x] += 1
        fw.add(height[x] + 1, 1)

        if fw.sum(base + 1) == 0:
            base += 1

    else:
        y = v
        need = base + y

        less = fw.sum(need)
        ans.append(N - less)

print(*ans, sep="\n")
