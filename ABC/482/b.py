S = []

for _ in range(5):
    S.append(input())

ans = 5

for i in range(5):
    cnt = 0
    for j in range(5):
        if S[i][j] == ".":
            cnt += 1
    ans = min(ans, cnt)
for j in range(5):
    cnt = 0
    for i in range(5):
        if S[i][j] == ".":
            cnt += 1
    ans = min(ans, cnt)

cnt = 0
for i in range(5):
    if S[i][i] == ".":
        cnt += 1
ans = min(ans, cnt)
cnt = 0
for i in range(5):
    if S[i][4 - i] == ".":
        cnt += 1
ans = min(ans, cnt)

print(ans)
