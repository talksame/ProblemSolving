height, width = map(int, input().split())
cnt = 0
if height == 1:
    cnt = 1
elif height == 2:
    cnt = min(4, int((width + 1) / 2))
elif width < 7:
    cnt = min(width, 4)
else:
    cnt = 5 + width - 7
print(cnt)