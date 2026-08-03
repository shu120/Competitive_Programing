# C - Distribution
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

ans = T[:]

for i in range(2 * N):
    curr = i % N
    nxt = (curr + 1) % N

    ans[nxt] = min(ans[nxt], ans[curr] + S[curr])

print(*ans, sep="\n")
