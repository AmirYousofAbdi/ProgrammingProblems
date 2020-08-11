n = int(input())
maghsoom = input().split(' ')
for i in range(len(maghsoom)):
    maghsoom[i] = int(maghsoom[i])
ls = []
for i in range(1, 1000 + 1):
    neshane = 1
    for j in range(len(maghsoom)):
        if i % maghsoom[j] == 0 and neshane != 0:
            neshane = 1
        else:
            neshane = 0
    if neshane == 1:
        ls.append(i)

t = 0
while t < len(ls):
    if ls.count(ls[t]) != 1:
        ls.pop(t)
        t = 0
    t += 1
print(len(ls))