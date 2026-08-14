N, V = map(int, input().split())

XD = []
max_d = 0

for _ in range(N):
    X, D = map(int, input().split())
    XD.append((X, D))
    max_d = max(max_d, D)


def check(K):
    _l = -(10**30)
    _r = 10**30

    for X, D in XD:
        need = (D + K - 1) // K

        if need > V:
            return False

        dist = V - need

        _l = max(_l, X - dist)
        _r = min(_r, X + dist)

        if _l > _r:
            return False

    return True


if not check(max_d):
    print(-1)
else:
    ng = 0
    ok = max_d

    while ok - ng > 1:
        mid = (ok + ng) // 2

        if check(mid):
            ok = mid
        else:
            ng = mid

    print(ok)
