T = int(input())

for _ in range(T):
    H, W = map(int, input().split())

    rev = False

    if H > W:
        H, W = W, H
        rev = True

    ans = []

    def add(r, c, s):
        if rev:
            ans.append((c, r, s))
        else:
            ans.append((r, c, s))

    # At least one is even
    if H % 2 == 0 or W % 2 == 0:
        h = H - H % 2
        w = W - W % 2

        for r in range(1, h + 1, 2):
            for c in range(1, w + 1, 2):
                add(r, c, 1)

    # Both are odd
    else:
        # H <= W
        # Process two columns at a time from the righ, Set to H * H
        while W > H:
            for r in range(1, H, 2):
                add(r, W - 1, 1)

            W -= 2

        # H x H odd sized square
        n = H
        r0 = 1
        c0 = 1

        while n >= 3:
            # square
            add(r0, c0, n - 1)

            # ↑
            for c in range(2, n - 1, 2):
                add(r0, c0 + c - 1, 1)

            # →
            for r in range(2, n - 1, 2):
                add(r0 + r - 1, c0 + n - 2, 1)

            # ↓
            for c in range(3, n, 2):
                add(r0 + n - 2, c0 + c - 1, 1)

            # ←
            for r in range(3, n, 2):
                add(r0 + r - 1, c0, 1)

            r0 += 2
            c0 += 2
            n -= 4

    print(len(ans))

    for r, c, s in ans:
        print(r, c, s)
