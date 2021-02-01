import sys
# sys.stdin = open("input.txt","rt")

a,b = map(int,input().split())
c=a
i=2
ans = []
ans.append(1)
ans.append(a)
while(a>i):
    if c%i == 0:
        if i == c//i :
            ans.append(i)
            a = c//i
        else :
            ans.append(i)
            ans.append(c//i)
            a = c//i

    i = i + 1

ans.sort()
if len(ans)<b :
    print(-1)
else :
    print(ans[b-1])

