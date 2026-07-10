#B - AcCepted
S = input()

if S[0] != "A":
    print("WA")

elif S[2:-1].count("C") != 1:
    print("WA")

else:
    c = S.index("C")

    T = S[1:c] + S[c+1:]

    if T.islower():
        print("AC")
    else:
        print("WA")
