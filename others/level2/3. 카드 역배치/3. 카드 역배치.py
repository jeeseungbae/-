import sys
# sys.stdin = open("input.txt","rt")

x = [i+1 for i in range(20)]

for _ in range(10):
    a,b = map(int,input().split())
    y = x.copy()

    for i in range(b-a+1):
        x[a-1+i] = y[b-1-i]

for i in x :
    print(i, end=" ")

