import sys
S = sys.stdin.readline().strip()
n = len(S)
s = [i for i in S]
for i in s:
    x = list(reversed(s))
    if s==x:
        break
    else:
        s.insert(n,i)
print(len(s))