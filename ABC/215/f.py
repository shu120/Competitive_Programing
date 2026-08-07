# F - Dist Max 2
N = int(input())

ten = []

for _ in range(N):
    x, y = map(int, input().split())
    ten.append((x, y))

ten.sort()


def check(k):
    j = 0
    min_y = float("inf")
    max_y = -float("inf")

    for i in range(N):
        x, y = ten[i]

        while j < i and x - ten[j][0] >= k:
            min_y = min(min_y, ten[j][1])
            max_y = max(max_y, ten[j][1])
            j += 1

        if y - min_y >= k or max_y - y >= k:
            return True

    return False


ok = 0
ng = 10**9 + 1

while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
