import sys
#sys.stdin = open("input.txt","rt")

T = int(input())

for i in range(T):
    N,s,e,k = map(int,input().split())
    a = list(map(int,input().split()))

    ans = a[s-1:e]
    ans.sort()

    print("#"+str(i+1)+" "+str(ans[k-1]))
