#ABC067 B - Snake Toy
N , K = map(int, input().split())
l = list(map(int, input().split()))

ans = 0
for i in range(1, K + 1):
	ans += sorted(l)[-i]

print(ans)