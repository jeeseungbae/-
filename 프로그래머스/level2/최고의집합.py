def solution(n, s):
    answer = []
    q = s//n
    a = []
    if q==0 :
        answer = [-1]
    elif s%n ==0 :
        answer.append(q)
        answer = answer * n
    else :
        answer.append(q)
        answer = answer*n
        for i in range(s%n):
            answer[i]=answer[i]+1
        answer.sort()
    return answer
