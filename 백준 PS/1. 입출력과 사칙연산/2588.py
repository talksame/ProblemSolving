'''
https://www.acmicpc.net/problem/2588

'''

a = int(input())
b = input()
listb = list(b)

line3 = a * int(b[2])
line4 = a * int(b[1])
line5 = a * int(b[0])

line6 = line3 + line4*10 + line5*100
print(line3)
print(line4)
print(line5)
print(line6)