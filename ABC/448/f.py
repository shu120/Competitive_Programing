#WA
import sys
input = sys.stdin.readline

N = int(input())

pts = []
for i in range(N):
	x, y = map(int, input().split())
	pts.append((x + y, i + 1))

start = 1
rest = pts[1:]

rest.sort()

ans = [1]
for _, idx in rest:
	ans.append(idx)

print(*ans)
