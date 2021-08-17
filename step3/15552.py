n=int(input())
sum=0

for i in range(n+1):
    sum=sum+i

print(sum)



#map사용해서 풀 수도 있음


import sys
t=int(sys.stdin.readline())

for i in range(t):
    a, b = map(int,(sys.stdin.readline()).split())
    print(a+b)
