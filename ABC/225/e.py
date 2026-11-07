# E - フ
# https://github.com/shu120/Competitive_Programing/blob/main/LIB/lib.py


def sort_cmp(data, cmp):
    """cmp_to_key を使わず、比較関数 cmp で安定マージソートで直接並べ替える。

    Parameter:
        data: 並べ替えるリスト。空リストも受け付ける。
        cmp: a を b より前に置くとき cmp(a, b) が True になる関数。
            同順位では False を返し、比較の順序に矛盾がないようにする。
    Return:
        None。data 自体を更新し、同順位の要素の元の順序を保つ。
    Order:
        要素数を N として時間 O(N log N)、追加領域 O(N)。比較は O(1) とする。
    使用例:
        sort_cmp(data, lambda a, b: a < b)  # 昇順（降順は a > b）
    """
    n = len(data)
    if n <= 1:
        return

    src = data[:]
    dst = [None] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            i, j = left, mid

            for k in range(left, right):
                if i < mid and (j == right or not cmp(src[j], src[i])):
                    dst[k] = src[i]
                    i += 1
                else:
                    dst[k] = src[j]
                    j += 1

        src, dst = dst, src
        width *= 2

    data[:] = src


N = int(input())

ans = 0
fu = []

for _ in range(N):
    x, y = map(int, input().split())

    right = (y, x - 1)
    left = (y - 1, x)

    fu.append((right, left))


def cmp(a, b):
    p1, q1 = a[0]
    p2, q2 = b[0]

    return p1 * q2 < p2 * q1


sort_cmp(fu, cmp)

curr = (0, 1)

for right, left in fu:
    p1, q1 = curr
    p2, q2 = left

    if p1 * q2 <= p2 * q1:
        ans += 1
        curr = right

print(ans)
