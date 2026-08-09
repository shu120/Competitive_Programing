import heapq

N = int(input())

ans = 0
MOD = 998244353
meeting = []

for _ in range(N):
    S, T = map(int, input().split())
    meeting.append((S, T))

meeting.sort()

q = []

for S, T in meeting:
    while q and q[0] <= S:
        heapq.heappop(q)

    if len(q) >= 2:
        print(0)
        exit()
    if not q:
        ans += 1

    heapq.heappush(q, T)

print(pow(2, ans, MOD))
