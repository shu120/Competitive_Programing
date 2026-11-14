N = int(input())
A = list(map(int, input().split()))

cnt = {}
ans = 1

cnt[A[0]] = 1

for i in range(1, N):
    if A[i] != A[i - 1]:
        same = cnt.get(A[i], 0)
        ans += i - same

    if A[i] not in cnt:
        cnt[A[i]] = 0

    cnt[A[i]] += 1

print(ans)
