import sys
# sys.stdin = open("input.txt","rt")

n= int(input())

answer = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

answer.sort()

for i in range(n-1):
    for j in range(i+1,n):
        if answer[i][1] < answer[j][1]:
            cnt+=1
            break

print(n-cnt)