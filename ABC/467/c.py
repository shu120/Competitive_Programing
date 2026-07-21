N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = N

for first in range(2):
    curr = first
    cnt = curr != A[0]

    for i in range(N - 1):
        curr ^= B[i]
        cnt += curr != A[i + 1]

    ans = min(ans, cnt)

print(ans)
