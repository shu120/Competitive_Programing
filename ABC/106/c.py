#C - To Infinity
S = input()
K = int(input())

for i in range(min(K, len(S))):
    if S[i] != '1':
        print(S[i])
        quit()

print('1')
