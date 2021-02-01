import sys
# sys.stdin = open("input.txt","rt")

def reverse(x):
    a = ""
    for i in str(x):
        a = i + a
    return int(a)

def isPrime(x):
    if x==1:
        return False;
    for i in range(2,x):
        if x%i==0:
            return False;
    else:
        return True;

N = int(input())
a = list(map(int,input().split()))

for i in a:
    x = reverse(i)
    if isPrime(x):
        print(x,end=" ")
