import sys
input = sys.stdin.readline
# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py


class SegTree:
    """Segment Tree
    0-indexed / 点更新・区間クエリ

    Parameters
    ----------
    A : list
        初期配列
    op : function
        2つの区間情報を結合する関数
    e : any
        opの単位元

    Methods
    -------
    update(i, x)
        A[i] を x に変更する
    query(left, right)
        閉区間 [left, right] の情報を取得する
    all_query()
        配列全体の情報を取得する
    """

    def __init__(self, A, op, e):
        self.op = op
        self.e = e
        self.n = len(A)

        # 葉の数を n 以上の最小の2冪にする
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # data[1] が根、data[size:] が葉
        self.data = [e] * (2 * self.size)

        # 葉に初期値を入れる
        for i in range(self.n):
            self.data[self.size + i] = A[i]

        # 下から順に親を構築する
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def update(self, i, x):
        """A[i] を x に変更する"""
        i += self.size
        self.data[i] = x

        # 更新した葉から根まで再計算
        while i > 1:
            i >>= 1
            self.data[i] = self.op(
                self.data[2 * i],
                self.data[2 * i + 1]
            )

    def query(self, left, right):
        """閉区間 [left, right] の情報を取得する"""
        left += self.size
        right += self.size

        # opが非可換でも使えるよう左右を分けて集計
        res_left = self.e
        res_right = self.e

        while left <= right:
            # left が右の子なら、その区間を採用
            if left & 1:
                res_left = self.op(
                    res_left,
                    self.data[left]
                )
                left += 1

            # right が左の子なら、その区間を採用
            if not (right & 1):
                res_right = self.op(
                    self.data[right],
                    res_right
                )
                right -= 1

            # 親へ移動
            left >>= 1
            right >>= 1

        return self.op(res_left, res_right)

    def all_query(self):
        """配列全体の情報を取得する"""
        return self.data[1]


N, Q = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**18

seg = SegTree(A, min, INF)

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        i = q[1] - 1
        x = q[2]
        seg.update(i, x)

    else:
        l = q[1] - 1
        r = q[2] - 1
        print(seg.query(l, r))
