import sys
input = sys.stdin.readline

SIZE = 10**6

N = int(input())
A = [0] * SIZE

for _ in range(N):
    S, V = input().split()
    A[int(S)] += int(V)

# 6次元累積和高速ゼータ変換
for base in [1, 10, 100, 1000, 10000, 100000]:
    for i in range(SIZE):
        if (i // base) % 10 != 0:
            A[i] += A[i - base]

Q = int(input())
out = []
bases = [100000, 10000, 1000, 100, 10, 1]

for _ in range(Q):
    x, y = input().split()

    xl = [ord(c) - 48 for c in x]
    yl = [ord(c) - 48 for c in y]

    ok = True
    for i in range(6):
        if xl[i] > yl[i]:
            ok = False
            break

    if not ok:
        out.append("0")
        continue

    ans = 0

    # 包除原理
    for mask in range(1 << 6):
        idx = 0
        sign = 1
        valid = True

        for i in range(6):
            if (mask >> i) & 1:
                d = xl[i] - 1
                sign *= -1
            else:
                d = yl[i]

            if d < 0:
                valid = False
                break

            idx += d * bases[i]

        if valid:
            ans += sign * A[idx]

    out.append(str(ans))

print("\n".join(out))
