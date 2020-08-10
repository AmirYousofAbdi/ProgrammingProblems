n = int(input())
jomle = input()
ls = []
jam = ''
for i in range(len(jomle)):
    if jomle[i] != ' ':
        jam += jomle[i]
    else:
        ls.append(jam)
        jam = ''
ls.append(jam)
ls.reverse()
jam = ''
for i in range(len(ls)):
    jam += ls[i] + ' '
print(jam)