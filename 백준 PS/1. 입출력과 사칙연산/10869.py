'''
https://www.acmicpc.net/problem/10869

'''

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
print(n + m)
print(n - m)
print(n * m)
print(n // m)
print(n % m)