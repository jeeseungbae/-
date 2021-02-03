import sys
# sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
m,n = max(n,m),min(n,m)
num = m-n+1

for i in range(num,0,-1):
    print(m + 2 - i,end=" ")


