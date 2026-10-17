N, M = map(int, input().split())

S = []
ans = [0] * N

for _ in range(N):
    S.append(input())

for _ in range(M):
    T = input()

    if T in S:
        ans[S.index(T)] += 1
        continue

    cand = -1
    cnt = 0

    for i in range(N):
        if len(S[i]) != len(T):
            continue

        diff = 0

        for j in range(len(T)):
            if S[i][j] != T[j]:
                diff += 1

        if diff == 1:
            cand = i
            cnt += 1

    if cnt == 1:
        ans[cand] += 1

for a in ans:
    print(a)
