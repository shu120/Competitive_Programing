N, K = map(int, input().split())

cloths = []

for _ in range(N):
    _l, r = map(int, input().split())
    cloths.append((_l, r))

cloths.sort(key=lambda x: x[1])


def can(d):
    count = 0
    last_r = -10**30

    for _l, r in cloths:
        if _l >= last_r + d:
            count += 1
            last_r = r

            if count == K:
                return True

    return False


if not can(1):
    print(-1)
else:
    ok = 1
    ng = 10**17

    while ng - ok > 1:
        mid = (ok + ng) // 2

        if can(mid):
            ok = mid
        else:
            ng = mid

    print(ok)
