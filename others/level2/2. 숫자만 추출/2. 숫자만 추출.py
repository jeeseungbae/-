import sys
# sys.stdin = open("input.txt","rt")

x = input()
num = ""
ans = 0
j=1

for i in x:
    if '0' <= i and i <= '9':
        num = num + i

num = int(num)
s = num

print(num)

while num>j:
    if s%j ==0:
        if s//j == j :
            ans = ans + 1
        else :
            ans = ans + 2
        num = s//j
    j+=1

if num==1:
    print(1)
else :
    print(ans)