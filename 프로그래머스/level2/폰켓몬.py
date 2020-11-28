def solution(nums):
    answer = 0
    a = len(set(nums))
    num = len(nums)//2
    
    if num >= a :
        answer = a
    else :
        answer = num
    
    return answer
