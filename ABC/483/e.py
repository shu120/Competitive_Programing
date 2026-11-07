# 参照:https://qiita.com/uni745e/items/9823ce5cd9c279a12d8a
from itertools import combinations

N, M = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

pair = [0] * (M + 1)

for k in range(M - 2, M + 1):
    for pos in combinations(range(M), k):
        cnt = {}

        for s in S:
            ptrn = ""

            for i in pos:
                ptrn += s[i]

            if ptrn not in cnt:
                cnt[ptrn] = 0

            pair[k] += cnt[ptrn]
            cnt[ptrn] += 1

hum0 = pair[M]
hum1 = pair[M - 1] - M * hum0
hum2 = pair[M - 2]
hum2 -= (M * (M - 1) // 2) * hum0
hum2 -= (M - 1) * hum1

print(hum0 + hum1 + hum2)
