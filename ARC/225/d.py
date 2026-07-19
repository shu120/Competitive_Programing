N = int(input())
P = list(map(int, input().split()))

ans = 0
for i, p in enumerate(P, 1):
    ans += abs(p - i)

print(ans // 2)
