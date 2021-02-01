import sys
# sys.stdin = open("input.txt","rt")

def samecount(x):
    for i in x:
        if x.count(i) > 1:
            return x.count(i),i
    else :
        return 1,max(x)

def price(cnt, x):
    if cnt == 1:
        return (10 ** 2) * x
    else:
        return (10 ** cnt) * (10 + x)


n = int(input())
answer = []

for i in range(n):
    a = list(map(int, input().split()))
    x,y = samecount(a)
    answer.append(price(x,y))

print(max(answer))





