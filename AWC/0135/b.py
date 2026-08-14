N = int(input())

best_p, best_s = map(int, input().split())
ans = 1

for i in range(2, N + 1):
    P, S = map(int, input().split())

    if S * best_p > P * best_s:
        best_p = P
        best_s = S
        ans = i

print(ans)
