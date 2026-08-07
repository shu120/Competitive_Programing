# A - Signed Difficulty
X, Y = input().split(".")

Y = int(Y)
ans = X
if 0 <= Y <= 2:
    ans += "-"
elif 3 <= Y <= 6:
    pass
else:
    ans += "+"

print(ans)
