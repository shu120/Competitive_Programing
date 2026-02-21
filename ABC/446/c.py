import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N, D = map(int, input().split())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	
	stock = 0
	rest = [0] * N
	cons = 0
	
	for i in range(N):
		# 朝
		stock += A[i]
		rest[i] = A[i]
		
		# 昼
		need = B[i]
		stock -= need
		
		while need > 0:
			if rest[cons] <= need:
				need -= rest[cons]
				rest[cons] = 0
				cons += 1
			else:
				rest[cons] -= need
				need = 0
		
		# 夜
		if i - D >= 0:
			stock -= rest[i - D]
			rest[i - D] = 0
	
	print(stock)