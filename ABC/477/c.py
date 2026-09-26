Q = int(input())
S = input()
T = input()

INF = len(S) + 1
nxt = [INF] * (INF)

for i in range(len(S) - 1, -1, -1):
    nxt[i] = nxt[i + 1]

    if i + len(T) <= len(S) and S[i:i + len(T)] == T:
        nxt[i] = i

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1

    if nxt[L] <= R - len(T) + 1:
        print("Yes")
    else:
        print("No")
