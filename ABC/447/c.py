S = input().strip()
T = input().strip()

if S.replace("A", "") != T.replace("A", ""):
	print(-1)
else:
	def f(s):
		res = []
		cnt = 0
		for c in s:
			if c == "A":
				cnt += 1
			else:
				res.append(cnt)
				cnt = 0
		res.append(cnt)
		return res

	a = f(S)
	b = f(T)

	print(sum(abs(x - y) for x, y in zip(a, b)))