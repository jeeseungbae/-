def solution(n):
    answer = ''
    a = '수박'*n
    for i in range(n) :
        answer = answer + a[i]
    return answer
