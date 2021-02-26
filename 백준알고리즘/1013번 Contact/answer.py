import re
import sys
sys.stdin = open("input.txt","rt")

a = int(input())
results = []

for _ in range(a):
    x = input()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(x)
    if m:
        print("YES")
    else:
        print("NO")
