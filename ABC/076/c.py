#C - Dubious Document 2
Sd = input()
T = input()

N = len(Sd)
M = len(T)

cand = []

for i in range(N - M + 1):
    flag = True
    for j in range(M):
        if Sd[i + j] != '?' and Sd[i + j] != T[j]:
            flag = False
            break
    if not flag:
        continue

    tmp = list(Sd)

    for j in range(M):
        tmp[i + j] = T[j]
    for k in range(N):
        if tmp[k] == '?':
            tmp[k] = 'a'
    cand.append(''.join(tmp))

if not cand:
    print("UNRESTORABLE")
else:
    print(min(cand))
