def solution(progresses, speeds):
    answer = []
    a = []
    for i, j in zip(progresses,speeds):
        pro = 100-i
        if j==1 :
            a.append(int(pro//(j)))
        else :
            a.append(int(pro//(j)+1))
    w = a[0]
    num = 1
    for i in range(1,len(a)) :
        if max(w,a[i]) != w :
            w = a[i]
            answer.append(num)
            num = 1
        else :
            num = num + 1
    answer.append(num)
    return answer
