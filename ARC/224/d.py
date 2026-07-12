import sys
input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N, K = map(int, input().split())

    if N < (K - 1).bit_length():
        ans.append("-1")
        continue

    lim = len(str(K))
    cnt = [0] * (lim + 1)

    p = 1

    for dig in range(1, lim + 1):
        q = p * 10
        cnt[dig] = min(K, q - 1) - p + 1
        p = q

    rem = K
    lvl = 0
    ways = 1
    dig = lim
    cost = 0

    while rem:
        use = min(ways, rem)
        rem -= use

        while use:
            num = min(use, cnt[dig])

            cost += lvl * dig * num
            use -= num
            cnt[dig] -= num

            if cnt[dig] == 0:
                dig -= 1

        lvl += 1

        if rem:
            ways = ways * (N - lvl + 1) // lvl
            ways = min(ways, rem)

    ans.append(str(cost))

print("\n".join(ans))
