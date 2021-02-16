import sys
# sys.stdin = open("input.txt","rt")


a = [[0,0] + list(map(int,input().split()))+ [0,0] for _ in range(7)]
a = [[0]*11] + [[0]*11] + a + [[0]*11] + [[0]*11]
cnt = 0

for i in range(2,9):
    for j in range(2,9):
        if (a[i][j-1]==a[i][j+1]) and (a[i][j-2]==a[i][j+2]):
            cnt+=1
        if (a[j-1][i]==a[j+1][i]) and (a[j-2][i]==a[j+2][i]):
            cnt+=1
print(cnt)
