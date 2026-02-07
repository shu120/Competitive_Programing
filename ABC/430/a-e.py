# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    a-e.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/01 20:56:45 by shukondo          #+#    #+#              #
#    Updated: 2026/02/07 22:20:08 by shukondo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#A
a, b, c, d = map(int, input().split())

if c >= a and d < b:
		print("Yes")
else:
	print("No")

#B
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

patt = set()
for i in range(N - M + 1):
	for j in range(N - M + 1):
		block = tuple(S[i + k][j:j + M] for k in range(M))
		patt.add(block)

print(len(patt))

#C
N, A, B = map(int, input().split())
S = input().strip()

cum_a = [0] * (N + 1)
cum_b = [0] * (N + 1)

for i in range(N):
	cum_a[i + 1] = cum_a[i] + (S[i] == 'a')
	cum_b[i + 1] = cum_b[i] + (S[i] == 'b')

ans = 0
ra = 0
rb = 0

for l in range(N):
	while ra < N and cum_a[ra + 1] - cum_a[l] < A:
		ra += 1
	while rb < N and cum_b[rb + 1] - cum_b[l] < B:
		rb += 1
	if ra < rb:
		ans += rb - ra

print(ans)

#D
from bisect import bisect_left, insort_left

N = int(input())
X = list(map(int, input().split()))

pos = [0]
dist = {0: float('inf')}
total = 0

for val in X:
	i = bisect_left(pos, val)
	nb = []
	if i > 0:
		nb.append(pos[i - 1])
	if i < len(pos):
		nb.append(pos[i])
	mydist = min(abs(val - u) for u in nb)
	for u in nb:
		total -= dist[u]
		dist[u] = min(dist[u], abs(val - u))
		total += dist[u]
	
	dist[val] = mydist
	total += mydist
	insort_left(pos, val)

	print(total)

#E

def solve():
	import sys
	input = sys.stdin.readline

	T = int(input())
	rslt = []

	for _ in range(T):
		A = input().strip()
		B = input().strip()

		if len(A) != len(B):
			rslt.append(-1)
			continue
		AA = A + A
		idx = AA.find(B)

		if 0 <= idx < len(A):
			rslt.append(idx)
		else:
			rslt.append(-1)

	print("\n".join(map(str, rslt)))

if __name__ == "__main__":
	solve()