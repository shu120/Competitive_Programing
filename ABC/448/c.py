import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

order = sorted((A[i], i+1) for i in range(N))

for _ in range(Q):
	K = int(input())
	B = set(map(int, input().split()))
	
	for v, idx in order:
		if idx not in B:
			print(v)
			break