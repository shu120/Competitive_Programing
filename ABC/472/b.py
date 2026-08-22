N = int(input())
L = list(map(int, input().split()))

s = sum(L)
left = 0
ans = s

for a in L[:-1]:
    left += a
    ans = min(ans, abs(s - 2 * left))

print(ans)
