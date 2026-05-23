N = int(input())
S = input().split()

ans = ""

for s in S:
    c = s[0]
    if c <= "c":
        ans += "2"
    elif c <= "f":
        ans += "3"
    elif c <= "i":
        ans += "4"
    elif c <= "l":
        ans += "5"
    elif c <= "o":
        ans += "6"
    elif c <= "s":
        ans += "7"
    elif c <= "v":
        ans += "8"
    else:
        ans += "9"

print(ans)
