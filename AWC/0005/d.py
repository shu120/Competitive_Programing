N, K = map(int, input().split())
A = list(map(int, input().split()))

def is_ok(x):
	count = 0
	current = 0
	for a in A:
		current += a
		if current >= x:
			count += 1
			current = 0
	return count >= K

def meguru_bisect(ng, ok):
	while ok - ng > 1:
		mid = (ok + ng) // 2
		if is_ok(mid):
			ng = mid
		else:
			ok = mid
	return ng

ng = 0
ok = sum(A) + 1

print(meguru_bisect(ng, ok))