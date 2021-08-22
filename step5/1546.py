n=int(input())
score = map(int,input().split())
score=list(score)
# print(max(score))
# print(type(score))
max_score=max(score)
new=[]
sum=0
for i in range(len(score)):
    new.append(score[i]/max_score*100)
    sum +=new[i]
    avg=sum/len(new)

print(avg)
