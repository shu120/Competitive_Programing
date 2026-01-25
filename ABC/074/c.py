#C - Sugar Water
import sys
input = sys.stdin.readline

A, B, C, D, E, F = map(int, input().split())

waters = set()
for i in range(31):
	for j in range(31):
		w = 100 * (A * i + B * j)
		if 0 < w <= F:
			waters.add(w)

sugars = set()
