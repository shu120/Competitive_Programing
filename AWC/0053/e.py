import sys
input = sys.stdin.readline

MOD = 998244353

N, M, K = map(int, input().split())

mat = [[0] * N for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    mat[u - 1][v - 1] = w % MOD


def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            if a[i][k] == 0:
                continue
            aik = a[i][k]
            bk = b[k]
            ri = res[i]
            for j in range(N):
                if bk[j] == 0:
                    continue
                ri[j] = (ri[j] + aik * bk[j]) % MOD
    return res


def mat_pow(base: list[list[int]], exp: int) -> list[list[int]]:
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        res[i][i] = 1

    while exp > 0:
        if exp & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        exp >>= 1

    return res


ans_mat = mat_pow(mat, K)
print(ans_mat[0][N - 1])
