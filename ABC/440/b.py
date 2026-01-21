#B - Trifecta
N = int(input())
T = list(map(int, input().split()))

horse = [(T[i], i + 1) for i in range(N)]
horse.sort()

print(horse[0][1], horse[1][1], horse[2][1])