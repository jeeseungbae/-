import sys
# sys.stdin = open("input.txt","rt")

a,b = map(int,input().split())
m = list(map(int,input().split()))
m.sort()
i = 0
half = len(m)//2 -1

while(1):
    if m[half] > b :
        half,a = (a-i)//2, half
    elif m[half] < b :
        half,i = (a+i)//2, half
    else :
        print(half+1)
        break











