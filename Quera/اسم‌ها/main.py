def str_to_list(name):
    ls = []
    for i in range(len(name)):
        ls.append(name[i])
    return ls
def tekrar(name):
    i = 0
    neshane = 0
    name = str_to_list(name)
    while i < len(name):
        if name.count(name[i]) > 1:
            name.pop(i)
            i = 0
        i += 1
    return len(name)
n = int(input())
ls = []
for i in range(n):
    ls.append(input())
b = 0
for i in range(n):
    if tekrar(ls[i]) > b:
        b = tekrar(ls[i])
print(b)