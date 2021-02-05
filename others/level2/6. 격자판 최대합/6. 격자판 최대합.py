import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]
ans = []
b,c = 0,0

for i in range(n):
    ans.append(sum(a[i]))  # 행 덧셈 나열
    ans.append(sum([a[j][i] for j in range(n)])) # 열 덧셈 나열
    b = b + a[i][i] # 대각선 덧셈
    c = c + a[n-i-1][i]

print(max(max(ans),b,c)) # 가장 큰값 찾기