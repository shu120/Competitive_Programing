from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1

    G[u].append((v, c))

first_color = [-1] * N
pending = [[] for _ in range(N)]

q = deque()
q.append((0, 0, 0))

ans = -1

while q:
    curr, color, dist = q.popleft()

    if curr == N - 1:
        ans = dist
        break

    if first_color[curr] == -1:
        first_color[curr] = color

        for nxt, nxt_color in G[curr]:
            if nxt_color == color:
                pending[curr].append((nxt, nxt_color))
            else:
                q.append((nxt, nxt_color, dist + 1))

    elif first_color[curr] != color:
        for nxt, nxt_color in pending[curr]:
            q.append((nxt, nxt_color, dist + 1))

        pending[curr] = []

print(ans)
# with AI
# 発想力が不足している 上位2つ持てばいいや！をコンテスト中に思いつく気がしなかった
