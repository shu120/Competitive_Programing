#010 - Score Sum Queries（★2）
import sys
input = sys.stdin.readline

N = int(input())
s1 = [0] * (N + 1)
s2 = [0] * (N + 1)

for i in range(N):
	C, P = map(int, input().split())
	s1[i + 1] = s1[i]
	s2[i + 1] = s2[i]
	if C == 1:
		s1[i + 1] += P
	else:
		s2[i + 1] += P

Q = int(input())
for _ in range(Q):
	L, R = map(int, input().split())
	print(s1[R] - s1[L - 1], s2[R] - s2[L - 1])