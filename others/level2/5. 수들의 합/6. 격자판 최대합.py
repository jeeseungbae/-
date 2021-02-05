import sys
# sys.stdin = open("input.txt","rt")

n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
cnt = 0

for i in range(n) :
    x = 0
    if sum(A) == m:
        cnt +=1
        break
    for j in range(i,n):
        x = x + A[j]
        if x>m : break
        elif x==m : cnt += 1

print(cnt)