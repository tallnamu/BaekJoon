n = []
div = []

for i in range(10):
    n.append(int(input()))
    div.append(n[i] % 42)

div2 = set(div)
#print(div)
print(len(div2))
