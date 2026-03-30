import sys
input = sys.stdin.readline

N = int(input())
C = [[0] * N for _ in range(N)]

for i in range(N - 1):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        C[i][j] = row[j - i - 1]
        C[j][i] = row[j - i - 1]

for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            if C[a][c] > C[a][b] + C[b][c]:
                print("Yes")
                exit()

print("No")
