# D - Online games
import heapq

N = int(input())

player = []

for _ in range(N):
    A, B = map(int, input().split())
    player.append((A, A + B))

player.sort()

ans = [0] * (N + 1)

hq = []
i = 0
day = 0

while i < N or hq:
    if not hq:
        day = player[i][0]

    while i < N and player[i][0] <= day:
        heapq.heappush(hq, player[i][1])
        i += 1

    nxt_start = player[i][0] if i < N else float("inf")
    nxt_end = hq[0]

    nxt_day = min(nxt_start, nxt_end)

    ans[len(hq)] += nxt_day - day
    day = nxt_day

    while hq and hq[0] == day:
        heapq.heappop(hq)

print(*ans[1:])
