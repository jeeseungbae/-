def solution(n):
    answer = 0
    num=0
    for i in range(1,n//2+1):
        a=0
        for j in range(i,n):
            a = a + j
            if a == n : 
                num=num+1 
                break
            elif a>n:
                break
    answer = num+1
    return answer
