N = int(input())
S = input()

ans = 0
curr = 0

for s in S:
    if s == "R":
        curr += 1
        ans = max(ans, curr)
    else:
        curr = 0

print(ans)
