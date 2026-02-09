N, K = map(int, input().split())
D = list(map(int, input().split()))

D.sort(reverse=True)
print(sum(D[K:]))