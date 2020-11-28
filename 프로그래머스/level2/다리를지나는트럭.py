def solution(bridge_length, weight, truck_weights):
    answer = 1
    w = []
    b = []
    num = []
    number= 0
    r = len(truck_weights)
    while len(b)!=0 or len(w)!=r:
        if sum(b)<weight and len(w) < r :
            b.append(truck_weights[number])
            w.append(truck_weights[number])
            num.append(bridge_length)
            number = number+1
            if (sum(b) > weight) :
                b.pop()
                w.pop()
                num.pop()
                number = number-1
        answer = answer + 1
        for i in range(len(num)) :
            num[i] = num[i]-1
        if num[0] == 0 :
            num.pop(0)
            b.pop(0)
            
    return answer
