def solution(n, words):
    answer = [0,0]
    a= []
    z=words[0][-1]
    for i in range(1,len(words)):
        if(words[i][0]==z):
            z = words[i][-1]
            if(words[0]==words[i]):
                answer = [i%n+1,i//n+1]
                break
            elif(words[i] in a):
                answer = [i%n+1,i//n+1]
                break
        else:
            answer = [i%n+1,i//n+1]
            break
        a.append(words[i])
    return answer
