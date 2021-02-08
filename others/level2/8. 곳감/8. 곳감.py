import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
num = int(input())
ans = 0

for _ in range(num) :
    b = list(map(int,input().split()))
    b[2] = b[2] % n
    if b[1] == 0 :
        a[b[0]-1][:] = a[b[0]-1][b[2]:] + a[b[0]-1][:b[2]]
    elif b[1] == 1 :
        a[b[0]-1][:] = a[b[0]-1][-b[2]:] + a[b[0]-1][:-b[2]]

for i in range(n//2):
    ans = ans + sum(a[i][i:n-i]) + sum(a[n-i-1][i:n-i])

print(ans + a[n//2][n//2])
