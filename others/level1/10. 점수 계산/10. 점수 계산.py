import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
x = list(map(int,input().split()))
ans = 0
num = 0

for i in x:
    if i == 1 :
        num = num + 1
    else :
        num = 0
    ans = ans + num

print(ans)