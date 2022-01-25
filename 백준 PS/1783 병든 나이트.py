width, height = map(int, input().split())

if height==1:
    print(1)

elif height==2:
    temp=[(width+1)//2,4]
    print(min(temp))

elif height>=3:
    if width>=7:
        print(width-2)
    else:
        temp=[4,width]
        print(min(temp))