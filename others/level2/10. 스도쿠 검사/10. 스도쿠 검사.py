import sys
sys.stdin = open("input.txt","rt")

x = [list(map(int,input().split())) for _ in range(9)]
y = sum(range(1,10))
answer = "YES"
dx = [0,3,6]
dy = [0,3,6]


for i in range(9):
    # 행 중복 제거하여 덧셈이 45여야한다.
    if y != sum(set(x[i])) \
            or y != sum(set([x[j][i] for j in range(9)])): # 열 중복 제거하여 덧셈이 45여야한다.
        answer = "NO"
        break
else:
    # 3 x 3 행렬 중복제거한 덧셈이 45여야 한다.
    for j in dy:
        for i in dx:
            if y != sum(set(x[j][i:i+3]+x[j+1][i:i+3]+x[j+2][i:i+3])) :
                answer = "NO"
                break

print(answer)

