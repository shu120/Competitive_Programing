import sys
from collections import deque
import random

input = sys.stdin.readline
random.seed(0)

DX = (-1, 1, 0, 0)
DY = (0, 0, -1, 1)

def get_candidates(N, M, owner, px, py):
	visited = [[False]*N for _ in range(N)]
	cand = [[False]*N for _ in range(N)]

	enemy_piece = [[False]*N for _ in range(N)]
	for p in range(1, M):
		enemy_piece[px[p]][py[p]] = True

	q = deque()
	x0, y0 = px[0], py[0]
	q.append((x0, y0))
	visited[x0][y0] = True

	reachable = []
	while q:
		x, y = q.popleft()
		reachable.append((x, y))
		for d in range(4):
			nx, ny = x + DX[d], y + DY[d]
			if 0 <= nx < N and 0 <= ny < N and (not visited[nx][ny]) and owner[nx][ny] == 0:
				visited[nx][ny] = True
				q.append((nx, ny))

	candidates = []
	for x, y in reachable:
		if not cand[x][y] and not enemy_piece[x][y]:
			cand[x][y] = True
			candidates.append((x, y))
		for d in range(4):
			nx, ny = x + DX[d], y + DY[d]
			if 0 <= nx < N and 0 <= ny < N:
				if (not cand[nx][ny]) and (not enemy_piece[nx][ny]):
					cand[nx][ny] = True
					candidates.append((nx, ny))
	return candidates

def min_enemy_dist(x, y, M, px, py):
	md = 10**9
	for p in range(1, M):
		d = abs(x - px[p]) + abs(y - py[p])
		if d < md:
			md = d
	return md if md != 10**9 else 10

def score_cell(t, x, y, N, M, U, V, owner, level, px, py):
	v = V[x][y]
	o = owner[x][y]
	l = level[x][y]

	md = min_enemy_dist(x, y, M, px, py)
	dist_mul = 1.0 + 0.18 * md

	if o == -1:
		expand_mul = 3.2 - 0.012 * t
		if expand_mul < 1.8:
			expand_mul = 1.8
		base = v * expand_mul

	elif o == 0:
		if l >= U:
			return 0.1 * v
		reinforce_mul = 1.6 + 0.35 * (U - l)
		base = v * reinforce_mul

	else:
		if l == 1:
			attack_mul = 2.6
		else:
			attack_mul = 0.25
		base = v * attack_mul

	future = 0
	for d in range(4):
		nx, ny = x + DX[d], y + DY[d]
		if 0 <= nx < N and 0 <= ny < N:
			if owner[nx][ny] == -1:
				future += 1

	future_mul = 1.0 + 0.3 * future

	return base * dist_mul * future_mul

def read_turn_result(N, M, owner, level, px, py):
	for _ in range(M):
		input().split()

	for p in range(M):
		ex, ey = map(int, input().split())
		px[p], py[p] = ex, ey

	for i in range(N):
		row = list(map(int, input().split()))
		for j in range(N):
			owner[i][j] = row[j]

	for i in range(N):
		row = list(map(int, input().split()))
		for j in range(N):
			level[i][j] = row[j]

def main():
	N, M, T, U = map(int, input().split())
	V = [list(map(int, input().split())) for _ in range(N)]

	sx = [0] * M
	sy = [0] * M
	for p in range(M):
		sx[p], sy[p] = map(int, input().split())

	owner = [[-1] * N for _ in range(N)]
	level = [[0] * N for _ in range(N)]
	px = sx[:]
	py = sy[:]
	for p in range(M):
		owner[sx[p]][sy[p]] = p
		level[sx[p]][sy[p]] = 1

	for t in range(T):
		candidates = get_candidates(N, M, owner, px, py)

		if random.random() < 0.06:
			tx, ty = random.choice(candidates)
		else:
			best = None
			best_s = -1e100
			for (x, y) in candidates:
				s = score_cell(t, x, y, N, M, U, V, owner, level, px, py)
				s *= 1.0 + (random.random() - 0.5) * 1e-6
				if s > best_s:
					best_s = s
					best = (x, y)
			tx, ty = best

		print(tx, ty, flush=True)
		read_turn_result(N, M, owner, level, px, py)

if __name__ == "__main__":
	main() 