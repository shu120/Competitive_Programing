N, M = map(int, input().split())

ans = [-1] * M

for _ in range(N):
    C, S = map(int, input().split())
    ans[C - 1] = max(ans[C - 1], S)

print(*ans)
