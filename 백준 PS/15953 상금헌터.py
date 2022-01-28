import sys
input = sys.stdin.readline

n = int(input())
f_2017 = sum(
    [[0], [500], [300] * 2, [200] * 3, [50] * 4, [30] * 5, [10] * 6]
    ,
    []
)

f_2018 = sum([[0], [512], [256] * 2, [128] * 4, [64] * 8, [32] * 16], [])

print(f_2017)
for _ in range(n):
    a, b = map(int, input().split())
    m1 = (f_2017[a] * 10000) if a < len(f_2017) else 0
    m2 = (f_2018[b] * 10000) if b < len(f_2018) else 0

    print(m1 + m2)