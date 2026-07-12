import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    S = input().strip()

    st = []
    ans = 0

    for c in S:
        if c == "A":
            st.append("A")

        elif c == "B":
            while st and st[-1] == "AB":
                st.pop()

            if st:
                st[-1] = "AB"
            else:
                ans += 1

        else:
            while st and st[-1] == "A":
                st.pop()

            if st:
                st.pop()
            else:
                ans += 1

    out.append(str(ans))

print("\n".join(out))
