# F - Parenthesis Checking

class SegTree:
    """Segment Tree
    0-indexed / 点更新・区間クエリ [l, r]
    """

    def __init__(self, A, op, e):
        self.op = op
        self.e = e

        n = len(A)
        self.size = 1
        while self.size < n:
            self.size <<= 1

        self.data = [e] * (2 * self.size)

        for i in range(n):
            self.data[self.size + i] = A[i]

        for i in range(self.size - 1, 0, -1):
            self.data[i] = op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def update(self, i, x):
        """A[i] を x に変更"""
        i += self.size
        self.data[i] = x

        while i > 1:
            i >>= 1
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def query(self, left, right):
        """[left, right] のクエリ"""
        left += self.size
        right += self.size

        res_left = self.e
        res_right = self.e

        while left <= right:
            if left & 1:
                res_left = self.op(res_left, self.data[left])
                left += 1

            if not (right & 1):
                res_right = self.op(self.data[right], res_right)
                right -= 1

            left >>= 1
            right >>= 1

        return self.op(res_left, res_right)


def merge(left, right):
    s1, mn1 = left
    s2, mn2 = right

    return (
        s1 + s2,
        min(mn1, s1 + mn2)
    )


N, Q = map(int, input().split())
S = list(input())

A = []

for c in S:
    if c == "(":
        A.append((1, 0))
    else:
        A.append((-1, -1))

seg = SegTree(A, merge, (0, 0))

for _ in range(Q):
    t, l, r = map(int, input().split())
    l -= 1
    r -= 1

    if t == 1:
        S[l], S[r] = S[r], S[l]

        if S[l] == "(":
            seg.update(l, (1, 0))
        else:
            seg.update(l, (-1, -1))

        if S[r] == "(":
            seg.update(r, (1, 0))
        else:
            seg.update(r, (-1, -1))

    else:
        total, mn = seg.query(l, r)

        if total == 0 and mn >= 0:
            print("Yes")
        else:
            print("No")
