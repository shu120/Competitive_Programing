N, M = map(int, input().split())

S = []

for _ in range(N):
    S.append(input())

for i in range(N):
    if S[i] == "x" * M:
        print("Faucet", i + 1)
        exit()

for j in range(M):
    if all(S[i][j] == "x" for i in range(N)):
        print("Drain", j + 1)
        exit()
