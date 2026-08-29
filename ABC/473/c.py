N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = [0] * N

for a in A:
    cnt[a - 1] += 1

max_cnt = max(cnt)

ans = 0

for c in cnt:
    if c + 1 >= max_cnt:
        ans += 1

print(ans)
