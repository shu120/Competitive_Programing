import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())

rows = {}

for _ in range(N):
    a, b = map(int, input().split())
    if a not in rows:
        rows[a] = []
    rows[a].append(b)

cross = W - 1

base_left = 0
base = 0
diff = []

for cols in rows.values():
    cols.sort()

    m = len(cols)

    cost_left = 2 * (cols[-1] - 1)
    cost_right = 2 * (W - cols[0])

    stay = min(cost_left, cost_right)

    for i in range(m - 1):
        cost = 2 * (cols[i] - 1) + 2 * (W - cols[i + 1])
        stay = min(stay, cost)

    base_left += cost_left
    base += stay
    diff.append(cross - stay)

ans = base_left

diff.sort()

extra = 0
for i, d in enumerate(diff):
    extra += d

    if (i + 1) % 2 == 0:
        ans = min(ans, base + extra)
    else:
        ans = min(ans, base + extra + cross)

ans = min(ans, base + 2 * cross)

print(ans)
