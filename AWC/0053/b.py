N = int(input())
X = list(map(int, input().split()))

X.sort()
med = X[N // 2]

ans = sum(abs(x - med) for x in X)

print(ans)
