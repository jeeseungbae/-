import sys
sys.stdin = open("input.txt","rt")

a,b = map(int,input().split())

c=a # 숫자 복사
i=2 # 나누기 2부터


ans = [] # 정답 순서대로 넣기
ans.append(1) # 1은 무조건 약수포함
ans.append(a) # 마지막 자기자신도 약수포함

while(a>i):
    if c%i == 0: # 나누어 떨어진다면?
        if i == c//i : #  5 X 5 등등 제곱수
            ans.append(i) # 하나의 값만 넣기
            a = c//i # 반복 횟수 줄이기
        else :
            ans.append(i) # i 값
            ans.append(c//i) # 몫
            a = c//i # 반복 횟수 줄이기
    i = i + 1 # 1씩 증가

ans.sort() # 순서대로

if len(ans)<b : # k번째가 없을 때
    print(-1)
else :
    print(ans[b-1])

