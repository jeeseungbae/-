import sys
# sys.stdin = open("input.txt","rt")

N = int(input())

ans = [i for i in range(2,N+1)]
answer = []

for i in ans :
    for j in range(2,i):
        if i%j==0:
            break
    else :
        answer.append(i)

print(len(answer))