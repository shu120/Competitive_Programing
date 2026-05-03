from collections import deque
import sys
input = sys.stdin.readline


def solve() -> str:
    N, M = map(int, input().split())

    G = [[v] for v in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        G[A].append(B)
        G[B].append(A)

    W = int(input())
    S = [input().strip() for _ in range(N)]

    total = N * W

    def idx(day: int, city: int) -> int:
        return day * N + city

    active = [False] * total
    active_cnt = 0

    for day in range(W):
        for city in range(N):
            if S[city][day] == "o":
                active[idx(day, city)] = True
                active_cnt += 1

    graph = [[] for _ in range(total)]
    indegree = [0] * total

    for day in range(W):
        next_day = (day + 1) % W

        for city in range(N):
            now = idx(day, city)

            if not active[now]:
                continue

            for next_city in G[city]:
                nxt = idx(next_day, next_city)

                if active[nxt]:
                    graph[now].append(nxt)
                    indegree[nxt] += 1

    q = deque()

    for v in range(total):
        if active[v] and indegree[v] == 0:
            q.append(v)

    removed = 0

    while q:
        v = q.popleft()
        removed += 1

        for nxt in graph[v]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    if removed < active_cnt:
        return "Yes"
    return "No"


T = int(input())

ans = []

for _ in range(T):
    ans.append(solve())

print("\n".join(ans))
