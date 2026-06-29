import sys

input = sys.stdin.readline

MAX_N = 2 * 10 ** 5

is_prime = [True] * (MAX_N + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, MAX_N + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    seen = set()
    ok = True

    for a in A:
        r = a % N
        if r in seen:
            ok = False
            break
        seen.add(r)

    if not ok:
        ans.append(0)
        continue

    if not is_prime[N]:
        ans.append(0)
        continue

    base = 1
    for d in range(1, N):
        base *= pow(d, N - d, N)
        base %= N

    pair = []

    for a in A:
        pair.append((a, a % N))

    pair.sort()

    bit = [0] * (N + 1)
    used_cnt = 0
    inv_guuki = 0

    for _, r in pair:
        x = r + 1

        cnt_leq = 0
        idx = x

        while idx > 0:
            cnt_leq += bit[idx]
            idx -= idx & -idx

        greater_cnt = used_cnt - cnt_leq

        if greater_cnt % 2 == 1:
            inv_guuki ^= 1

        idx = x

        while idx <= N:
            bit[idx] += 1
            idx += idx & -idx

        used_cnt += 1

    if inv_guuki == 1:
        ans.append((-base) % N)
    else:
        ans.append(base)

print("\n".join(map(str, ans)))
