N, K = map(int, input().split())
A = list(map(int, input().split()))


def can(x: int) -> bool:
    need = 0

    for i, a in enumerate(A, start=1):
        if a < x:
            need += (x - a + i - 1) // i
            if need > K:
                return False

    return True


ok = min(A)
ng = max(A) + K * N + 1

while ng - ok > 1:
    mid = (ok + ng) // 2
    if can(mid):
        ok = mid
    else:
        ng = mid

print(ok)
