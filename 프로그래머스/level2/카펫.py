def solution(brown, yellow):
    answer = []
    
    for i in range(1,brown+1):
        if (brown+yellow)%i==0 :
            a=max((brown+yellow)/i,i)
            b=min((brown+yellow)/i,i)
            if (a-2)*(b-2)==yellow:
                answer.append(a)
                answer.append(b)
                break
    
    return answer
