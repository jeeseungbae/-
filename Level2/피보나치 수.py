def solution(n):
    answer = 0
    a = []
    a.append(0)
    a.append(1)
    for i in range(0,n):
        a.append(a[i]+a[i+1])
    answer = a[n]%1234567
    return answer
