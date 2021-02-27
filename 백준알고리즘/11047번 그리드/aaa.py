import sys
sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
ans = [int(input()) for _ in range(n)]
cnt = 0

for i in range(len(ans)-1,-1,-1):
    if k//ans[i]!=0:
        cnt += k//ans[i]
        k = k%ans[i]
print(cnt)
