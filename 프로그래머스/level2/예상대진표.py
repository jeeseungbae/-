def solution(n,a,b):
    answer = 0
    
    while n>1 :
        if (min(a,b)%2==1 and max(a,b)%2==0 and min(a,b)+1 ==max(a,b)):
            answer=1
            break
        elif (a>n and b>n) or (a <= n and b <= n) :
            if (a>n and b>n) :
                a = a - n
                b = b - n
            n = n//2
        else :
            while max(a,b)>1:
                a = (a+1)//2
                b = (b+1)//2
                answer = answer+1
            break
    return answer
