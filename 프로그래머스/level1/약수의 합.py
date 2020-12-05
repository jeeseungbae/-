def solution(n):
    answer = 0
    w = n
    a = 1
    if n==1 :
        answer = n
    while n>a :
        if w%a == 0 :
            answer = answer + w//a + a
            if w//a == a :
                answer = answer - a
            n = w//a
        a=a+1
    return answer
