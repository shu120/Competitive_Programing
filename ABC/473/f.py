class SegTree:
    def __init__(self, A):
        n = len(A)
        self.size = 1

        while self.size < n:
            self.size <<= 1

        self.data = [(0, 0)] * (2 * self.size)

        for i in range(n):
            self.data[self.size + i] = A[i]

        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.merge(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def merge(self, left, right):
        s1, mn1 = left
        s2, mn2 = right

        return (
            s1 + s2,
            min(mn1, s1 + mn2)
        )

    def update(self, i, x):
        i += self.size
        self.data[i] = x

        while i > 1:
            i >>= 1
            self.data[i] = self.merge(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def query(self, left, right):
        left += self.size
        right += self.size

        res_left = (0, 0)
        res_right = (0, 0)

        while left <= right:
            if left & 1:
                res_left = self.merge(
                    res_left,
                    self.data[left]
                )
                left += 1

            if not (right & 1):
                res_right = self.merge(
                    self.data[right],
                    res_right
                )
                right -= 1

            left >>= 1
            right >>= 1

        return self.merge(res_left, res_right)


N = int(input())
S = list(input())
Q = int(input())

A = []

for c in S:
    if c == "A":
        A.append((1, 0))
    else:
        A.append((-1, -1))

seg = SegTree(A)

for _ in range(Q):
    q = input().split()

    if q[0] == "1":
        i = int(q[1]) - 1
        c = q[2]

        S[i] = c

        if c == "A":
            seg.update(i, (1, 0))
        else:
            seg.update(i, (-1, -1))

    else:
        left = int(q[1]) - 1
        right = int(q[2]) - 1

        s, mn = seg.query(left, right)

        if mn >= 0:
            print("Yes")
        else:
            print("No")
