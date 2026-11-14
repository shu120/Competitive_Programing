# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py
import sys
input = sys.stdin.readline


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


INF = 10**12
N, Q = map(int, input().split())
A = list(map(int, input().split()))

A_min = []
A_max = []

for x in A:
    if x == -1:
        A_min.append(INF)
        A_max.append(0)
    else:
        A_min.append(x)
        A_max.append(x)

seg_min = SegTree(A_min, min, INF)
seg_max = SegTree(A_max, max, 0)

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        i, x = q[1] - 1, q[2]

        if x == -1:
            seg_min.update(i, INF)
            seg_max.update(i, 0)
        else:
            seg_min.update(i, x)
            seg_max.update(i, x)

    else:
        left, right = q[1] - 1, q[2] - 1

        mn = seg_min.query(left, right)
        mx = seg_max.query(left, right)

        if mn == INF or mn == mx:
            print("Yes")
        else:
            print("No")
