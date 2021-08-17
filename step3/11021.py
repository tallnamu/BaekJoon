t=int(input())


for i in range(1,t+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print("Case #" +str(i)+":",a+b)




#다른 방법
T = int(input())

for i in range(1,T+1):
    a,b = map(int, input().split())
    print("Case #"+str(i)+':',a+b)
