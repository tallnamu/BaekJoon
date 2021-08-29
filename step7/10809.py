#10809

s=input()
alphabet=list(range(97,123)) #아스키코드 숫자 범위

for i in alphabet:
    print(s.find(chr(i)))
