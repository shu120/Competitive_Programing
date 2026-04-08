#C - HSI
N, M = map(int, input().split())

ans = (1900 * M + 100 * (N - M)) * (2 ** M)
print(ans)
