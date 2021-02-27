import sys
sys.stdin = open("input.txt","rt")

n = int(input())

ans = [list(map(int,input().split())) for _ in range(n)]
time = [0]*24
num = []

print(ans)




