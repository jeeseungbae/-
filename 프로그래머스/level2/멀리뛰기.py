def solution(n):
    answer = 0
    num = n//2
    
    for i in range(num+1):
        ft=1
        a = n-i*2
        t = a+i
        for x in range(t,0,-1):
            ft=ft*x
            if x <=i : ft = ft//x
            if x <=a : ft = ft//x
        answer = answer+ft
        
    return answer%1234567
