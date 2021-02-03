import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

for i in range(n):
    x = input().lower()
    if x == x[::-1] :
        print("#"+str(i+1) +" YES")
    else :
        print("#"+str(i+1) +" NO")
