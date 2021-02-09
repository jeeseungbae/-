import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

w = [[0]+list(map(int,input().split()))+[0] for _ in range(n)]
w = [[0]*(n+2)]+w+[[0]*(n+2)]
# 행렬에  0으로 감싸기

cnt=0

for i in range(n):
    for j in range(n):
        if w[i+1][j+1] > w[i+1][j] and \
                w[i+1][j+1] > w[i+1][j+2] and \
                w[i+1][j+1] > w[i+2][j+1] and \
                w[i+1][j+1] > w[i][j+1]:
            cnt+=1

print(cnt)
