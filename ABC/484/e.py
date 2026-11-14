# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py
from bisect import bisect_left, bisect_right


def compress(A):
    """値の大小関係を保ったまま、配列を 0 始まりの連続した整数に変換する。

    Parameter:
        A: 要素同士を大小比較でき、set・dict のキーとして使える値の配列。
    Return:
        各要素を昇順での順位に置き換えた新しいリスト。同じ値は同じ順位になる。
        A は変更せず、空配列には空リストを返す。
    Order:
        要素数を N、異なる値の数を K として時間 O(N + K log K)、追加領域 O(N + K)。
        ハッシュ操作は平均 O(1)、値の比較は O(1) とする。
    使用例:
        compress([30, 10, 30, 20])  # [2, 0, 2, 1]
    """
    vals = sorted(set(A))
    comp = {v: i for i, v in enumerate(vals)}
    return [comp[x] for x in A]


class Fenwick_Tree:
    """配列の一点への加算と区間和の取得を行う Fenwick Tree（fw）。

    仕様:
        添字は 1 始まり。初期値はすべて 0。
        add(i, v) で加算し、sum(i) で前方和、range_sum(left, right) で区間和を得る。
        区間は両端を含む。添字の範囲チェックは行わない。
    Order:
        要素数を N として初期化は時間・領域 O(N)。各操作は時間 O(log N)。
    """

    def __init__(self, n):
        """全要素が 0 の配列を管理する fw を初期化する。

        Parameter:
            n: 要素数（0 以上）。使用する添字は 1 から n。
        Return:
            None。長さ n + 1 の内部配列を作成する。
        Order:
            時間 O(n)、領域 O(n)。
        """
        self.n = n
        self.fw = [0] * (n + 1)

    def add(self, i, v):
        """指定した要素に値を加算する。

        Parameter:
            i: 更新する添字。1 <= i <= self.n。0 は指定しない。
            v: 加算する値。負の値を指定すると減算になる。
        Return:
            None。管理する配列の i 番目の値を v だけ増やす。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def sum(self, i):
        """閉区間 [1, i] の和を取得する。

        Parameter:
            i: 区間の右端。0 <= i <= self.n。
        Return:
            1 番目から i 番目までの合計。i = 0 のときは 0。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        s = 0

        while i > 0:
            s += self.fw[i]
            i -= i & -i

        return s

    def range_sum(self, left, right):
        """両端を含む指定区間の和を取得する。

        Parameter:
            left: 区間の左端。1 <= left <= right。
            right: 区間の右端。right <= self.n。
        Return:
            閉区間 [left, right] の合計。
        Order:
            時間 O(log N)、追加領域 O(1)。N は要素数。
        """
        return self.sum(right) - self.sum(left - 1)


N, L, R = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)

for i in range(N):
    S[i + 1] = S[i] + A[i]

rank_S = compress(S)
pos = sorted(set(S))
fw = Fenwick_Tree(len(pos))

ans = 0

for i, sr in enumerate(S):
    left = sr - R
    right = sr - L

    l_idx = bisect_left(pos, left) + 1
    r_idx = bisect_right(pos, right)

    ans += fw.sum(r_idx) - fw.sum(l_idx - 1)

    fw.add(rank_S[i] + 1, 1)

print(ans)
