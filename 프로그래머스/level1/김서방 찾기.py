def solution(seoul):
    answer = ''
    y=0
    for a in seoul :
        if 'Kim' == a :
            answer = "김서방은 {}에 있다".format(y)
        y = y+1
    return answer
