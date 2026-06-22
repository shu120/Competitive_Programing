#D - Xor Sum 2
N = int(input())
A = list(map(int, input().split()))

ans = 0
r = 0
x = 0

for l_ in range(N):
    while r < N and x & A[r] == 0:
        x ^= A[r]
        r += 1

    ans += r - l_

    if r == l_:
        r += 1
    else:
        x ^= A[l_]

print(ans)
