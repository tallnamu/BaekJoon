while True:
    try:
        a, b = input().split()
        a=int(a)
        b=int(b)
    except:
        break
    print(a+b)


#다른 방법

while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)
