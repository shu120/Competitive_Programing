import sys
input = sys.stdin.readline


def max_extra(active, U):
    active = set(active)

    if len(active) == 1:
        i = next(iter(active))
        if i == 0:
            return min(U[0], U[1])
        if i == 1:
            return min(U[1], U[2])
        return min(U[2], U[0])

    if len(active) == 2:
        if active == {0, 1}:
            return min(U[1], U[0] + U[2])
        if active == {1, 2}:
            return min(U[2], U[1] + U[0])
        return min(U[0], U[2] + U[1])

    s = sum(U)
    m = max(U)
    return min(s, 2 * (s - m)) // 2


def solve_case(a, b, c):
    n = [a, b, c]
    ans = 0

    for mask in range(1, 8):
        active = [i for i in range(3) if (mask >> i) & 1]

        low = [0, 0, 0]
        for i in active:
            low[i] = 1

        U = []
        ok = True

        for g in range(3):
            need = 1 if ((g - 1) % 3) in active else 0

            u = n[g] - need - low[g] - low[(g - 1) % 3]

            if u < 0:
                ok = False
                break

            U.append(u)

        if not ok:
            continue

        ans = max(ans, len(active) + max_extra(active, U))

    for i in range(3):
        if n[i] == n[(i + 1) % 3] and n[i] >= 2 and n[(i + 2) % 3] == 0:
            ans = max(ans, n[i])

    return ans


T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    print(solve_case(a, b, c))
