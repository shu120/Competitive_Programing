#002 - Encyclopedia of Parentheses

def solve(s, open_cnt, close_cnt, N):
	if len(s) == N:
		print(s)
		return
	if open_cnt < N // 2:
		solve(s + '(', open_cnt + 1, close_cnt, N)
	if close_cnt < open_cnt:
		solve(s + ')', open_cnt, close_cnt + 1, N)

N = int(input())
if N % 2 == 0:
	solve("", 0, 0, N)