import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
	N = int(input())
	reindeer = []
	total_power = 0

	for j in range(N):
		w, p = map(int, input().split())
		reindeer.append(w + p)
		total_power += p

	reindeer.sort()

	cnt = 0
	cur = 0
	for c in reindeer:
		if cur + c <= total_power:
			cur += c
			cnt += 1
		else:
			break

	print(cnt)