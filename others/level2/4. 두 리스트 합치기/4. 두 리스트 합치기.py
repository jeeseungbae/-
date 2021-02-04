import sys
# sys.stdin = open("input.txt","rt")

x = []

for _ in range(2):
    a  = int(input())
    b = list(map(int,input().split()))
    x = x+ b

x.sort()

for i in x:
    print(i,end=" ")