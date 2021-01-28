import sys
# sys.stdin = open("input.txt","rt")

x = int(input())
score = list(map(int,input().split()))
a = [0,0.0]

scoreMean = round(sum(score)/x,0)
# round를 쓰면 안된다. round_half_even방식 = 짝수쪽으로 근삿값 이동함
#ex) round(4.5) = 4출력됨 round(4.51) = 5출력
#정확히 4.5일때 문제
#round(5.5) = 6출력

score2 = list(map(abs,map(lambda x:x-scoreMean,score)))

for i in range(len(score2)) :
    if score2[i] == min(score2) and a[1] < score[i]:
        a[0] = i+1
        a[1] = score[i]

print(int(scoreMean),a[0])






