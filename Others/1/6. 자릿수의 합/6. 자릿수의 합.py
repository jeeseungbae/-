import sys
# sys.stdin = open("input.txt","rt")

def digit_sum(x):
    num = 0
    while(x>0):
        a = x%10
        x = x//10
        num = num + a
    return num

n = int(input())
x = list(map(int,input().split()))
max = 0

for i in x :
    if max<digit_sum(i):
        max = digit_sum(i)
        ans = i

print(ans)


