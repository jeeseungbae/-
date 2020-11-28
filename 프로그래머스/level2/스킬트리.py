def solution(skill, skill_trees):
    answer = 0
    for a in skill_trees:
        b = [a.find(i) for i in skill ]
        c = [a.find(i) for i in skill ]
        b.sort()
        d = len(b)
        for i in range(d) :
            if b[i] == -1:
                b.append(b[i])
                b.remove(b[i])
        if c == b :
            answer = answer+1
    return answer
