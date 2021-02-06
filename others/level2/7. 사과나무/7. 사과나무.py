import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

s = [list(map(int,input().split())) for _ in range(n)]
ans = 0
d = n//2    # 반을 기준으로 함
for i in range(d):
    ans = ans + sum(s[i][(d-i):(d+i+1)])    # 첫번째 항에서부터 반을 기준으로 i만큼  증가
    ans = ans + sum(s[d-1][(d-i):(d+i+1)])  # 마지막 항에서부터 반을 기준으로 i만큼 증가

print(ans + sum(s[(d)]))    # 중간 항 까지 더하기