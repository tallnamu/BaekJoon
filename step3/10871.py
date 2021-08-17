n, x = input().split()
a = list(input().split())
n=int(n)
x=int(x)

for i in range(n):
    if int(a[i] )< x:
        print(int(a[i]),end=' ')



#다른 방법
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")
