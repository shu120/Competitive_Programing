N, W = map(int, input().split())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0

for bit in range(1 << N):
    taste = 0
    vol = 0

    for i in range(N):
        if bit >> i & 1:
            taste += A[i]
            vol += B[i]

    if vol <= W:
        ans = max(ans, taste)

print(ans)
