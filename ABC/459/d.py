from collections import Counter

T = int(input())

for _ in range(T):
    S = input()
    N = len(S)

    cnt = Counter(S)

    if max(cnt.values()) > (N + 1) // 2:
        print("No")
        continue

    chars = []
    for c, n in cnt.items():
        chars.extend([c] * n)

    chars.sort(key=lambda c: -cnt[c])

    ans = [""] * N
    idx = 0

    for c in chars:
        ans[idx] = c
        idx += 2
        if idx >= N:
            idx = 1

    print("Yes")
    print("".join(ans))
