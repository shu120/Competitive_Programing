N, V = map(int, input().split())
W = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if (i + 1) + (j + 1) + (k + 1) <= V:
                ans = max(ans, W[i] + W[j] + W[k])

print(ans)
