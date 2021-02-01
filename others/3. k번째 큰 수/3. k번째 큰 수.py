# import sys
# sys.stdin = open("input.txt","rt")


def answerfind(N,K,ans):
    cnt = 0;
    answer = []

    for a in range(len(ans)):
        for b in range(a+1, len(ans)):
            for c in range(b+1, len(ans)):
                cnt += 1
                answer.append(ans[a]+ans[b]+ans[c])
    return answer

N,K = list(map(int,input().split()))
ans = list(map(int,input().split()))
ans.sort(reverse=True)

answer = list(set(answerfind(N,K,ans)))
answer.sort(reverse=True)

print(answer[K-1])



