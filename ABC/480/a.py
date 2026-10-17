S1 = input()
S2 = input()

if S1[0] + S2[1] in ["AD", "DA"]:
    print("No")
elif S1[1] + S2[0] in ["AD", "DA"]:
    print("No")
else:
    print("Yes")
