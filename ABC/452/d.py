import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

n = len(S)
m = len(T)

pos = [-1] * m
start = 0
ans = 0

for r in range(n):
    c = S[r]

    for j in range(m - 1, -1, -1):
        if c == T[j]:
            if j == 0:
                pos[0] = r
            elif pos[j - 1] != -1:
                pos[j] = pos[j - 1]

    if pos[m - 1] != -1:
        start = pos[ m- 1] + 1

    ans += r - start + 1

print(ans)
